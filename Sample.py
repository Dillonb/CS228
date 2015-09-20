import os, sys, inspect, thread, time
from pylab import *
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class SampleListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        ion()
        fig = plt.figure()
        ax = fig.add_subplot( 111 )
        ax.set_xlim(0,0)
        ax.set_ylim(0,0)
        xPt = 0
        yPt = 0
        pt, = plot(xPt,yPt,'ko',markersize=20)
        self.pt = pt
        self.ax = ax

    def on_frame(self, controller):
        frame = controller.frame()
        draw()

        #print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
        #    frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))
        
        if (frame.hands):
            hand = frame.hands[0]
            indexFinger = [finger for finger in hand.fingers if finger.type == finger.TYPE_INDEX][0]
            print indexFinger.joint_position(3)

            x = indexFinger.joint_position(3)[0]
            y = indexFinger.joint_position(3)[1]


            if x < self.ax.get_xlim()[0]:
                self.ax.set_xlim(x, self.ax.get_xlim()[0])
            if x > self.ax.get_xlim()[1]:
                self.ax.set_xlim(self.ax.get_xlim()[0], x)

            if y < self.ax.get_ylim()[0]:
                self.ax.set_ylim(y, self.ax.get_ylim()[0])
            if y > self.ax.get_ylim()[1]:
                self.ax.set_ylim(self.ax.get_ylim()[0], y)


            self.pt.set_xdata(indexFinger.joint_position(3)[0])
            self.pt.set_ydata(indexFinger.joint_position(3)[1])



def main():
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        print "dying"
        controller.remove_listener(listener)





if __name__ == "__main__":
    main()

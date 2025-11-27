import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimplePublisher(Node):

    def __init__(self):
        super().__init__('simple_publisher')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1.0, self.publish_message)

    def publish_message(self):
        msg = String()
        msg.data = 'Hello from Docker ROS2 Publisher 🚀'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)
    node = SimplePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

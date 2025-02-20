from launch import LaunchDescription

from launch.actions import (
    DeclareLaunchArgument,
    ExecuteProcess,
    OpaqueFunction
)

from launch.substitutions import (
    LaunchConfiguration
)

# This is needed to get the runtime value of the rosbag path for the ExecuteProcess
def launch_rosbag_record(context):
    rosbag_path: str = LaunchConfiguration('rosbag_path').perform(context)

    print("___________________________________________________________")
    print(rosbag_path)
    print("___________________________________________________________")

    rosbag_record = ExecuteProcess(
        cmd=['ros2', 'bag', 'record', '-a', '-o', rosbag_path],
        output='screen'
    )

    return [rosbag_record]

def generate_launch_description():
    rosbag_path_arg = DeclareLaunchArgument('rosbag_path',
                          default_value='/tmp',
                          description='Absolut path where the rosbag is saved')
    
    opfunc = OpaqueFunction(function = launch_rosbag_record)

    return LaunchDescription(
        [
            rosbag_path_arg,
            opfunc
        ]
    )
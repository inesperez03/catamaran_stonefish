import os
from launch import LaunchDescription
from launch.actions import GroupAction, IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution, EnvironmentVariable, Command
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    rviz_config_file = PathJoinSubstitution([
        EnvironmentVariable("HOME"),
        "entornos_stonefish", "src", "catamaran_stonefish", "config", "catamaran.rviz"
    ])


    description_file_cirtesu = PathJoinSubstitution([
        FindPackageShare("catamaran_stonefish"),
        "urdf", "cirtesu", "cirtesu.urdf.xacro"
    ])

    robot_description_cirtesu = Command([
        "xacro", " ",
        description_file_cirtesu
    ])
    
    namespace_action = GroupAction(
        actions=[
            IncludeLaunchDescription(
                PathJoinSubstitution([
                    FindPackageShare('stonefish_ros2'), 'launch', 'stonefish_simulator.launch.py'
                ]),
                launch_arguments={
                    'simulation_data': PathJoinSubstitution([
                        FindPackageShare('catamaran_stonefish'), 'data'
                    ]),
                    'scenario_desc': PathJoinSubstitution([
                        FindPackageShare('catamaran_stonefish'), 'scenarios', 'catamaran_cirtesu_arucos.scn'
                    ]),
                    'simulation_rate': '50.0',
                    'window_res_x': '1200',
                    'window_res_y': '800',
                    'rendering_quality': 'high'
                }.items()
            ),
        ]
    )
    return LaunchDescription([
        namespace_action])

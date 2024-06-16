import argparse
import shlex
from json_parser import read_json
from visualizer.visualizer_factory import VisualizerFactory
from icons.icon_factory import IconFactory


def process_command(command):
    # 使用argparse解析命令行参数
    parser = argparse.ArgumentParser(description='Funny JSON Explorer (FJE)')
    parser.add_argument('-f', '--file', required=True, help='Path to the JSON file')
    parser.add_argument('-s', '--style', choices=VisualizerFactory.get_styles(), default='tree',
                        help='Visualization style')
    parser.add_argument('-i', '--icon', choices=IconFactory.get_families(), default='default', help='Icon family')

    try:
        # 移除 "fje" 前缀并解析参数
        args = parser.parse_args(shlex.split(command))
        json_data = read_json(args.file)
        # 使用工厂方法模式创建相应的Visualizer对象和Iterator对象
        visualizer, IteratorClass, VisitorClass = VisualizerFactory.create_visualizer(args.style)
        json_root = visualizer.build_tree(json_data)
        visitor = VisitorClass()
        iterator = IteratorClass(json_root)

        # 使用抽象工厂模式创建相应的IconFamily对象
        icons = IconFactory.create_icon_family(args.icon)
        icon_family = icons.get_icons()
        # 可视化JSON数据
        visualizer.visualize(icon_family, iterator, visitor)
    except argparse.ArgumentError as e:
        print("Error:", e)
        print("Use 'fje -h' for help.")
    except Exception as e:
        print("An error occurred:", e)


def main():
    print("Welcome to Funny JSON Explorer (FJE)")
    print("Enter your command in the format: fje -f <json file> -s <style> -i <icon family>")
    print("Type 'exit' or 'quit' to exit the program.")

    while True:
        try:
            command = input("> ")
            if command.strip().lower() in ['exit', 'quit']:
                print("Exiting Funny JSON Explorer. Goodbye!")
                break

            # 确保命令以 "fje" 开头
            if not command.startswith("fje"):
                print("Invalid command. Commands should start with 'fje'.")
                continue

            # 去掉 "fje" 前缀并处理命令
            command = command[len("fje"):].strip()
            process_command(command)
        except (EOFError, KeyboardInterrupt):
            print("\nExiting Funny JSON Explorer. Goodbye!")
            break


if __name__ == '__main__':
    main()

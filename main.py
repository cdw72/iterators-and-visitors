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

        # 工厂方法模式：根据指定的样式创建具体的Visualizer、Iterator、Visitor对象
        visualizer, IteratorClass, VisitorClass = VisualizerFactory.create_visualizer(args.style)

        # 使用Visualizer对象构建树形结构
        json_root = visualizer.build_tree(json_data)

        # 使用Visitor模式创建相应的访问者对象
        # 访问者模式：允许在不改变数据结构的前提下添加新的操作
        visitor = VisitorClass()

        # 使用Iterator模式创建相应的迭代器对象
        # 迭代器模式：提供一种方法顺序访问一个聚合对象中的各个元素，而不暴露其内部的表示
        iterator = IteratorClass(json_root)

        # 使用抽象工厂模式创建相应的IconFamily对象
        # 抽象工厂模式：提供一个接口，用于创建相关或依赖对象的家族，而不需要明确指定具体类
        icons = IconFactory.create_icon_family(args.icon)
        icon_family = icons.get_icons()

        # 使用Visualizer对象进行可视化
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

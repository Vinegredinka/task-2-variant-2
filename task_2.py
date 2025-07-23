import argparse
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET


def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    x_data = [float(x.text) for x in root.find('xdata')]
    y_data = [float(y.text) for y in root.find('ydata')]

    return x_data, y_data


def plot_graph(x_data, y_data, title=None):
    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data, linewidth=2)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    if title:
        plt.title(title)
    else:
        plt.title('Graph of y = f(x)')
    plt.show()


def main():
    parser = argparse.ArgumentParser(description='Plot graph from XML data file')
    parser.add_argument('input_file', help='Path to input XML file')
    parser.add_argument('--title', help='Title for the plot')

    args = parser.parse_args()

    if not args.input_file.endswith('.xml'):
        print("Error: Input file must be in XML format")
        return

    try:
        x_data, y_data = parse_xml(args.input_file)
        plot_graph(x_data, y_data, args.title)
    except FileNotFoundError:
        print(f"Error: File {args.input_file} not found")
    except ET.ParseError:
        print(f"Error: Invalid XML format in {args.input_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
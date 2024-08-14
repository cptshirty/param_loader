from jinja2 import Environment, FileSystemLoader
import json
import glob
import argparse
import datetime
from pathlib import Path
import shutil

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='param_file', required=True)
    parser.add_argument('-o', dest='output_directory', required=True)
    args = parser.parse_args()
    # create full paths
    output_path = Path().resolve() / args.output_directory
    templates_path = Path(__file__).resolve().parent / 'templates'
    core_path = Path(__file__).resolve().parent / 'core'
    
    # setup jinja2 environment & templates
    env = Environment(loader=FileSystemLoader(templates_path))
    env.trim_blocks = True
    env.lstrip_blocks = True
    
    inc_template = env.get_template(name='params.h.j2')
    src_template = env.get_template(name='params.c.j2')
    sorter_inc_template = env.get_template(name='param_loader.h.j2')
    sorter_src_template = env.get_template(name='param_loader.c.j2')
    cmake_template = env.get_template(name='CMakeLists.txt.j2')

    file = args.param_file
    # delete output directory if it exists
    if output_path.exists():
        shutil.rmtree(output_path)
    sources = []
    headers = []
    topic_dict_list = []
    # load topic json file
    f = open(file)
    param_dict = json.load(f)
    # generate header
    filename = f'{output_path}/inc/params.h'
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    content = inc_template.render(param_dict=param_dict,date=datetime.date.today())
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)

    #generate source
    filename = f'{output_path}/src/params.c'
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    content = src_template.render(param_dict=param_dict,date=datetime.date.today())
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)

    filename = f'{output_path}/inc/param_loader.h'
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    content = sorter_inc_template.render(param_dict=param_dict,date=datetime.date.today())
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)

    #generate source
    filename = f'{output_path}/src/param_loader.c'
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    content = sorter_src_template.render(param_dict=param_dict,date=datetime.date.today())
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)


    #generate Cmake
    filename = f'{output_path}/CMakeLists.txt'
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    content = cmake_template.render(param_dict=param_dict,date=datetime.date.today())
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)


if __name__ == "__main__":
    main()

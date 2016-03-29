# encoding = utf-8
import os


def resolve_dir(path, source_path, target_path):
    path = str(path)
    if not os.path.isdir(path):
        pass
    else:
        files = os.listdir(path)
        for file in files:
            # if file.startswith("."):
            #     continue
            new_path = path + "/" + file
            if os.path.isdir(new_path):
                if not os.path.exists(target_path + "/" + file):
                    os.mkdir(target_path + "/" + file)
                resolve_dir(new_path, source_path, target_path + "/" + file)
            else:
                resolve_file(new_path, source_path, target_path)


def resolve_file(path, source_path, target_path):
    path = str(path)
    print(path)
    new_path = path.split("/")[-1]
    if path.endswith(".java"):
        try:
            java_file = open(path, "r")
            new_file = open(target_path + "/" + new_path, "w", encoding="utf-8")
            for line in java_file:
                new_file.write(line)
        except UnicodeDecodeError:
            java_file = open(path, "r", encoding="utf-8")
            new_file = open(target_path + "/" + new_path, "w", encoding="utf-8")
            for line in java_file:
                new_file.write(line)
        java_file.close()
        new_file.close()
    else:
        open(target_path + "/" + new_path, "wb").write(open(path, "rb").read())


source_path = "/yumei/code"
target_path = "/yumei/code_new"

resolve_dir(source_path, source_path, target_path)

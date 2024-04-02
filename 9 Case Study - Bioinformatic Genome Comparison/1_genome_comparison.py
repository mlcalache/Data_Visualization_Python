import matplotlib.pyplot as plt


def read_fasta_file(filename):
    x = open(filename).readlines()[1:]
    x = "".join(x)
    x = x.replace("\n", "")
    return x


def write_html_result(filename, data, rgb):
    x = open(filename, "w")

    w = 1
    transparency = 0
    for q in data:
        transparency = data[q] / max(data.values())
        x.write(
            "<div style='width:100px; border:1px solid #111; height:100px; float:left; background-color:rgba(" + rgb +
            "," + str(transparency) + "); color: #fff'>" + q + "</div>")
        if w % 4 == 0:
            x.write("<div style='clear:both'></div>")
        w += 1

    x.close()


def write_html_combined_result(filename, data_human, data_bacteria, rgb):
    x = open(filename, "w")

    x.write("<div style='clear:both'>Human</div>")

    w = 1
    for q in data_human:
        transparency = data_human[q] / max(data_human.values())
        x.write(
            "<div style='width:100px; border:1px solid #111; height:100px; float:left; background-color:rgba(" + rgb +
            "," + str(transparency) + "); color: #fff'>" + q + "</div>")
        if w % 4 == 0:
            x.write("<div style='clear:both'></div>")
        w += 1

    x.write("<div style='clear:both'>Bacteria</div>")

    w = 1
    for q in data_human:
        transparency = data_bacteria[q] / max(data_bacteria.values())
        x.write(
            "<div style='width:100px; border:1px solid #111; height:100px; float:left; background-color:rgba(" + rgb +
            "," + str(transparency) + "); color: #fff'>" + q + "</div>")
        if w % 4 == 0:
            x.write("<div style='clear:both'></div>")
        w += 1

    x.close()


def create_combinations(param_input):
    combinations = {}

    for i in ['A', 'T', 'C', 'G']:
        for j in ['A', 'T', 'C', 'G']:
            combinations[i + j] = 0

    for k in range(len(param_input) - 1):
        combinations[param_input[k] + param_input[k + 1]] += 1

    return combinations


bacteria_input = read_fasta_file("bacteria.fasta")
human_input = read_fasta_file("human.fasta")

bacteria = create_combinations(bacteria_input)
human = create_combinations(human_input)

write_html_result("bacteria.html", bacteria, '0,0,255')
write_html_result("human.html", human, '0,0,255')

write_html_combined_result("combined.html", human, bacteria, '0,0,255')

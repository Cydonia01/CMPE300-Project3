import subprocess

for i in range(3):
    for j in range(3):
        for k in range(3):
            process = subprocess.run(
                ['python', 'main.py'],
                input=f'{i+1}\n{j+1}\n{k+1}\nexit\n',
                text=True
            )
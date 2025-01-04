import subprocess

for i in range(4):
    for j in range(2):
        for k in range(3):
            if j == 0:
                for m in range(3):
                    for n in range(3):
                        process = subprocess.run(
                            ['python', 'main.py'],
                            input=f'{i+1}\n{j+1}\n{k+1}\n{m+1}\n{n+1}\nexit\n',
                            text=True
                        )
            else:
                for n in range(3):
                    process = subprocess.run(
                        ['python', 'main.py'],
                        input=f'{i+1}\n{j+1}\n{k+1}\n{n+1}\nexit\n',
                        text=True
                    )
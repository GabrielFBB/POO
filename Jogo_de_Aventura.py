
print("Bem vindo a Mansão assombrada!")
print("Muito cuidado ao entrar e com as decisões que tiver.")
print("Assim que você entra na mansão você se depara com uma escolha ir para a sala de estar ou para a sala de jantar ?")
### Prompt user for a choice
roomChoice = input("> ")

if(roomChoice == "sala de estar"):
  print("Você entrou na sala de estar.")
  print("Assim que você entra enxerga um pitbull guardando uma obra de arte.")
  print("Você quer tentar roubar o quadro que o pitbull está guardando ?")

  pitBullChoice = input("> ")

  if(pitBullChoice == "sim"):
    print("Você tenta roubar o quadro silenciosamente, porém o pitbull acorda e você acaba virando a janta dele")
    print("Você Morreu.")
  elif(pitBullChoice == "não"):
    print("Você decide deixar o cachorro e a obra de arte para trás.")
    print("Você dá meia volta e vai embora.")
  else:
    print("Escolha inválida. Por favor insira sim ou não.")
elif(roomChoice == "sala de jantar"):
  print("Você decide ir checar a sala de jantar.")
  print("Ao entrar você vê um pequeno báu.")
  print("Você deseja abri-lo ?")

  vaseChoice = input("> ")

  if(vaseChoice == "sim"):
    print("Você abre o báu e encontra uma espada cheia de runas,quando você pega nela ela começa a brilhar intensamente !")
    print("Logo em seguida vem um homem enorme com caninos avantajados correndo pra cima de você, sem pensar duas vezes você vira a espada na direção dele e ele vira pó na sua frente.")
    print("Depois dessa experiência você decide sair da casa com vida.")
  elif(vaseChoice == "não"):
    print("Você decide deixar o báu do jeito que está.")
    print("Assim que você se vira para partir você escuta a porta da sala se abrindo.")
    print("Um vulto preto vem correndo em sua direção e você sente uma dor no pescoço até que ela cessa.")
    print("Você Morreu.")
  else:
    print("Escolha inválida. Por favor insira sim ou não.")
else:
  print("Escolha inválida. Por favor insira sala de estar ou sala de jantar.")

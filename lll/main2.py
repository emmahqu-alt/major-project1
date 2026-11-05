 def question_page():
        page.controls.clear()
        Question=["What is your name",
                  "what is your age",
                  "What is your gender",
                  "what is your favorite color",
                  "What do you do in your rest time",
                  "what is your hobbies",
                  "what is your personlity",
                  "which color do you like,pink or bule",
                  "what is your favorite music type",
                  "Do you prefer study alone"]
        Questionanswer= [ft.TextField(label= x, hint_text = "Enter your answer") for x in Question]
        def choosen(e):
            data=[]
            new_person = {}
            for x in range(len(Question)):
                new_person[Question[x]] = Questionanswer[x].value
                data.append(new_person)
            for x in data:
                 if x["username"]==current_user[0]:
                      x["answers"]=new_person
            save_data(data)

        page.floating_action_button = ft.FloatingActionButton(content = "choosen",on_click = choosen)
        Register=ft.Button(content="register",on_click=register_click)
        page.updata
    def login_page():
        page.controls.clear()
        greeting = ft.Text(value="Hello, welcome to Lover Test!")
        username = ft.TextField(label = "Name", hint_text="Please enter your user name")
        password = ft.TextField(label = "Password", password=True)
        passwordconfirm = ft.TextField(label = "Confirm your Password", password=True)
        feedback=ft.text()
        def login(e):
            data=load_data()
            found=False
            for x in data:
                if x["username"]==username.value:
                    if x["password"]==password.value:
                        found=True
                        current_user[0]=username.value
            if found:
                 question_page
            else:
                 print("Wrong username and password")
                 page.update()
        
        
                        

        page.add(
             ft.Container(
                  expand=True,
                  content=ft.Column(
                       controuls=[
                            greeting,
                            username,
                            password,
                            passwordconfirm,
                            feedback,
                            login,
                            Register
                       ]
                       
                  ),alignment=ft.Alignment.CENTER
             )
        )
                            

    login_page()

ft.run(main)




 "What is your gender",
               "what is your favorite color",
               "What do you do in your rest time",
               "what is your hobbies",
               "what is your personlity",
               "which color do you like,pink or bule",
               "what is your favorite music",
               "Do you prefer study alone"

        
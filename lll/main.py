import flet as ft
import json

def main(page: ft.Page):
    page.title = "Zhang Test"
    page.window_width = 400
    page.window_height = 500
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ALWAYS
    page.title = "Background image"
    #Place the background picture
    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        image = ft.DecorationImage(
            src="background.jpg  ",
            fit= ft.BoxFit.FILL, 
        )
    )


    # First main page function have register page and login page
    def main_page():
        page.controls.clear()
        page.floating_action_button = None
        greeting = ft.Text(value="Hello, welcome to LOVERTES!")
        username = ft.TextField(label = "Name", hint_text="Please enter your user name")
        password = ft.TextField(label = "Password", password=True,can_reveal_password=True)
        feedback=ft.Text(size=16)
        #Control the user's login and judge whether the user has registered before
        def submit_click(e):
            data = {}
            with open("data.json", 'r') as f:
                data = json.load(f)
            if username.value in data:
                if data[username.value][0] == password.value:
                    feedback.value = ("Login successfully")
                    menu_page(username.value)
                else:
                    feedback.value = ("Incorrect password")
            else:
                feedback.value = ("Username does not exist")


        def register_click(e):
            register_page()




        page.floating_action_button = ft.FloatingActionButton("Register", on_click=register_click)
        Login = ft.Button(content = "Login", on_click=submit_click)
        page.add(
            ft.Container(
                expand = True,
                content = ft.Column(
                    controls = [
                        greeting,
                        username,
                        password,
                        Login,
                        feedback
                ]
                )
            )
        )


    # Second page function for user registration.It is used to remember the user's username and password
    def register_page():
        page.controls.clear()
        page.floating_action_button = None
        greeting = ft.Text(value="Please register for a new account")
        username = ft.TextField(label = "Name", hint_text="Please enter your user name")
        password = ft.TextField(label = "Password", password=True,can_reveal_password=True)
        passwordconfirm = ft.TextField(label = "Confirm your Password", password=True,can_reveal_password=True)
        feedback = ft.Text(size=16)
        def register_click(e):
            if password.value == passwordconfirm.value:
                data: dict = {}
               
                with open('data.json', 'r') as f:
                    data = json.load(f)
                # Add new user data to the JSON file with an empty list for questionnaire answers  
                data[username.value] = [password.value,[]]
                with open('data.json', 'w') as f:
                    json.dump(data, f)




                main_page()
            else:
                feedback.value = ("Passwords do not match")

        page.floating_action_button = ft.FloatingActionButton("Proceed", on_click=register_click)
        page.add(
            ft.Container(
                expand = True,
                content = ft.Column(
                    controls = [
                        greeting,
                        username,
                        password,
                        passwordconfirm,
                        feedback
                ]
                )
            )
        )


    # Third page function for user menu,have test ,back to the longin and matching pages
    def menu_page(username):
        page.controls.clear()
        greeting=ft.Text("Welocome,"+username)
        def test_click(e):
            questions_page(username)
        def match_click(e):
            matching_page(username)
        def logout_click(e):
            main_page()
        test=ft.Button("Take the test",on_click=test_click)
        match=ft.Button("Find your match",on_click=match_click)
        logout=ft.Button("Logout",on_click=logout_click)
        page.add(
            ft.Column(
                [
                    greeting,
                    test,
                    match,
                    logout
                ],
                alignment=ft.MainAxisAlignment.CENTER
   
            )
        )
   
    # Fourth page function for user questionnaire,includes validation for all questions
    def questions_page(username):
         page.controls.clear()
         page.floating_action_button=None
         Question=["What is your name",
                  "what is your age",
                  "What is your gender"
                   ]
         Questionanswer= [ft.TextField(label= x, hint_text = "Enter your answer") for x in Question]
         feedback=ft.Text()
         question4=ft.RadioGroup(
             content=ft.Column([
                ft.Radio(value="pink", label="pink"),
                ft.Radio(value="blue", label="blue"),
                ft.Radio(value="yellow", label="yellow"),
             ])
         )
         question5=ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="reading", label="reading"),
                ft.Radio(value="writting", label="writting"),
                ft.Radio(value="listening music", label="listening music"),
            ])
         )
         question6=ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="drawing", label="drawing"),
                ft.Radio(value="running", label="running"),
                ft.Radio(value="cooking", label="cooking"),
            ])
         )
         question7=ft.RadioGroup(
                 content=ft.Column([
                     ft.Radio(value="kind", label="kind"),
                     ft.Radio(value="quiet", label="quiet"),
                     ft.Radio(value="enthusiastic", label="enthusiastic"),
                 ])
             )
         question8=ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="True", label="True"),
                ft.Radio(value="false", label="false"),
            ])
         )
         question9=ft.RadioGroup(
                 content=ft.Column([
                     ft.Radio(value="Rock and roll", label="Rock and roll"),
                     ft.Radio(value="Folk song", label="Folk song"),
                     ft.Radio(value="classical music", label="classical music"),
                 ])
         )
         question10=ft.RadioGroup(
                 content=ft.Column([
                     ft.Radio(value="yes", label="yes"),
                     ft.Radio(value="no", label="no"),
                 ])
         )
         feedback = ft.Text(size=16)
         
         def save_click(e):
            if not Questionanswer[0].value:
                feedback.value="please enter your name"
                return
            if not Questionanswer[1].value:
                feedback.value="please enter your age"
                return
            if not Questionanswer[2].value:
                feedback.value="please enter your gender"
                return
            if not question4.value:
                feedback.value="please answer question4"
                return
            if not question5.value:
                feedback.value="please answer question5"
                return
            if not question6.value:
                feedback.value="please answer question6"
                return
            if not question7.value:
                feedback.value="please answer question7"
                return
            if not question8.value:
                feedback.value="please answer question8"
                return
            if not question9.value:
                feedback.value="please answer question9"
                return
            if not question10.value:
                feedback.value="please answer question10"
                return
            answer=[
                    Questionanswer[0].value,
                    Questionanswer[1].value,
                    Questionanswer[2].value,
                    question4.value,
                    question5.value,
                    question6.value,
                    question7.value,
                    question8.value,
                    question9.value,
                    question10.value
            ]
           
            with open("data.json", "r") as f:
                data = json.load(f)
            data[username][1] = answer
            with open("data.json", "w") as f:
                json.dump(data, f)
            feedback.value="Your answer have been saved"
         def back_click(e):
            menu_page(username)
               
         page.add(
            ft.Column(
                [
                    ft.Text("LOVER TEST"),
                    Questionanswer[0],
                    Questionanswer[1],
                    Questionanswer[2],
                    ft.Text("4.what is your favorite color"),
                    question4,
                    ft.Text("5.What do you do in your rest time"),
                    question5,
                    ft.Text("6.what is your hobbies"),
                    question6,
                    ft.Text("7.what is your personlity"),
                    question7,
                    ft.Text("8.Do you think people who smoke in public are right"),
                    question8,
                    ft.Text("9.what is your favorite music type"),
                    question9,
                    ft.Text("10.Do you prefer study alone"),
                    question10,
                    ft.Button("Save",on_click=save_click),
                    feedback,
                    ft.Button("Back",on_click=back_click)
                ],
                alignment=ft.Alignment.CENTER
            )
        )


    # Fifth page function for matching users based on their questionnaire answers    
    def matching_page(username):
        page.controls.clear()
        title=ft.Text("Your Matching Result")
        result=ft.Text()
        feedback=ft.Text()
        def find_match(e):
            data={}   
        with open("data.json", "r") as f:
            data = json.load(f)
        #Get my questionnaire answers
        my_answer=data[username][1]
        if len(my_answer)!=10:
            feedback.value="Please complete your questionnaire first."
        else:
            best_name=""
            best_score=-1
            #Find the option that best matches the users answer,compare the two people's answers
            for other_name in data:
                if other_name !=username:
                    other_answer=data[other_name][1]
                    if len(other_answer)==10:
                        score=0
                        if my_answer[3]==other_answer[3]:
                            score=score+1
                        if my_answer[4]==other_answer[4]:
                            score=score+2
                        if my_answer[5]==other_answer[5]:
                            score=score+3
                        if my_answer[6]==other_answer[6]:
                            score=score+4
                        if my_answer[7]==other_answer[7]:
                            score=score+1
                        if my_answer[8]==other_answer[8]:
                            score=score+2
                        if my_answer[9]==other_answer[9]:
                            score=score+2
                        if score>best_score:
                            best_score=score
                            best_name=other_answer[0]
            if best_name=="":
                result.value="NO other users have completed the test yet"
            else:
                percentage=best_score/15*100
                result.value=("Your best match is :"+best_name+
                                "\nMatching score:"+str(best_score)+"/15"+
                                "\nMatching percentage:"+str(percentage)+"%")
            feedback.value=""                  
        def back_click(e):
            menu_page(username)
        Find=ft.Button("Find match",on_click=find_match)
        Back=ft.Button("Back",on_click=back_click)
        page.add(
                ft.Column(
                    [
                        title,
                        Find,
                        Back,
                        result,
                        feedback
                       
                    ]
                )
            )
           


    main_page()


ft.run(main)




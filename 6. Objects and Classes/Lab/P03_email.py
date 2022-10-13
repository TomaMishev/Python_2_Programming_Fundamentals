# Create class Email. The __init__ method should receive sender, receiver and a content. It should also have a default
# set to False attribute called is_sent. The class should have two additional methods: •	send() - sets the is_sent
# attribute to True •	get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {
# is_sent}" You will receive some information (separated by a single space) until you receive the command "Stop". The
# first element will be the sender, the second one – the receiver, and the third one – the content. On the final
# line, you will be given the indices of the sent emails separated by comma and space ", ". Call the send() method
# for the given indices of emails. For each email, call the get_info() method.


class Email:

    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        text = f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
        return text


email = []
command = input()
while command != "Stop":
    command_line = command.split(" ")
    current_sender = command_line[0]
    current_receiver = command_line[1]
    current_content = command_line[2]

    current_email = Email(current_sender, current_receiver, current_content)
    email.append(current_email)
    command = input()
indexes = list(map(int, input().split(", ")))
for i in indexes:
    email[i].send()
for i in email:
    print(i.get_info())

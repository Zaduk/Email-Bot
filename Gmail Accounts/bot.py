import imaplib
import email
from email.header import decode_header


def select_mailbox(inbox):
    # select the mailbox you want
    imap.select(str(inbox))
    # print imap.list() to print all mailboxes


def search_by_sender(sender):
    # search for specific mails by sender
    status, messages = imap.search(None, 'FROM {}"'.format(sender))


def search_by_subject(subject):
    # to get mails by subject
    status, messages = imap.search(None, 'SUBJECT {}}'.format(subject))


def get_all_emails_in_inbox(inbox):
    # to get all mails
    status, messages = imap.search(None, "{}".format(inbox))


def delete_all_in_inbox(inbox):

    select_mailbox(inbox)

    for mail in messages:
        _, msg = imap.fetch(mail, "(RFC822)")
        # you can delete the for loop for performance if you have a long list of emails
        # because it is only for printing the SUBJECT of target email to delete
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    # if it's a bytes type, decode to str
                    subject = subject.decode()
                print("Deleting", subject)
        # mark the mail as deleted
        imap.store(mail, "+FLAGS", "\\Deleted")

    # permanently remove mails that are marked as deleted
    # from the selected mailbox (in this case, INBOX)
    imap.expunge()
    # close the mailbox
    imap.close()
    # logout from the account
    imap.logout()


if __name__ == '__main__':
    print("First, let's log you into your email.")
    # email_address = str(input(Email address: ))
    username = ""  # enter username
    # passphrase = str(input(Password: ))
    password = ""  # enter pass

    # log in
    # make an IMAP4 class using Secure Socket Layers security protocol
    imap = imaplib.IMAP4_SSL("imap.gmail.com")

    # actually log into account
    imap.login(username, password)
    print("You are now logged in.\n")
    option = int(input("What would you like to do?"))



# Assisted by WCA@IBM
# Latest GenAI contribution: ibm/granite-20b-code-instruct-v2

def isPalindrome(string):
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False

        left += 1
        right -= 1

    return True

#reverse linked list
def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev



if __name__ == '__main__':
    string = input("Enter a string: ")

    if isPalindrome(string):
        print("The input string is a palindrome.")
    else:
        print("The input string is not a palindrome.")

"""Write a function AMCount() in Python, which should read each character of a text file STORY.TXT,
should count and display the occurrences of alphabets A and M (including small cases a and m too)."""
def AMCount():
    with open("STORY.txt","r") as file:
        count = {"a":0,"m":0}
        words = file.read().lower()
        for characters in words:
            if characters in count:
                count[characters] += 1
    return count
dict = AMCount()
for i in dict:
    print(i,":",dict[i])
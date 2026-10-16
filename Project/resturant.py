d1={
    "pizza":150,
    "pasta":80,
    "momos":70,
    "fries":90,
    "ice creame":30,
    "coffee":100,
}
print("👋 🥂 ✨ Welcome ! TO Dnyaneshwaries Restaurant...✨ 🥂 👋")
print("Menus:")
print("🍕 Pizza:Rs.150\n🍝 Pasta: Rs.80\n🥟 Momos (Dumplings): Rs.70\n🍟 Fries:Rs.90\n🍦/🍧 Ice Creame:Rs.30\n☕ Coffee:Rs.100")
total=0

while True:
    item=input("Enter the name of item that you want to order=").lower()
    if item in d1:
         total+=d1[item]
         print(f"Your item {item} added to your order")
    else:
         print(f"Sorry...but your item {item} is not avaible yet !")
    item1=input("Do you want to order another item?(YES/No)=").lower()
    if item1!="yes":
      break
bill=input("can we give your total bill? (yes/no)=")
if bill.lower()=="yes":
     print(f"Your total  bill to pay is = {total}Rs.")

print("✨ Thank you for visiting the Python Restaurant! ✨")
print(" 🤗 Come back soon for more delicious bytes!")
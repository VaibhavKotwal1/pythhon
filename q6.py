"""
write a function called discount price that takes original price and 
discount as aparameter and print the final price after dicount 
"""
def discount_price(original_price,discount_percent):
    discount_amount=(discount_percent/100) * original_price
    final_amount=original_price - discount_amount 
    print(f"your will get dicount of Rs .{discount_amount} ")
    print(f"your final amount is Rs .{final_amount} ")

discount_price(100,50)    
discount_price(554840,50)    

    
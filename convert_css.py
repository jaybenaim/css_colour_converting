import cssutils 
import webcolors 

sheet = cssutils.parseFile('main.css')

def main(): 
    f= open("new_css.css", "a+") 
        
    for rule in sheet: 
        if rule.type == rule.STYLE_RULE: 
            # find property 
            for property in rule.style:
                if property.name == 'color':
                    if property.value != 'inherit': 
                        if property.value[0] != "#": 
                            property.value = webcolors.CSS3_NAMES_TO_HEX[property.value]
                    # property.priority = 'IMPORTANT'
    sheet.add('@import "sheets/main.css";')

# new = cssutils.parseFile(sheet.cssText)
# # print(sheet.cssText)
# print(new) 


    new = cssutils.parseFile(sheet.cssText)
    f.write(new)
    f.close() 

if __name__=="__main__": 
    main() 


# # Write to a new file
# with open('style_new.css', 'wb') as f:
#     f.write(sheet.cssText)



# css = u''' 
# html | a { color: red; font-family: arial; }
# ''' 
# sheet = cssutils.parseString(css) 


# for rule in sheet:
#     if rule.type == rule.STYLE_RULE:
#         # find property
#         for property in rule.style:

#             if property.name == 'color':

#                 property.value = 'green'
#                 property.priority = 'IMPORTANT'
#                 break
#         # or simply:
#         rule.style['margin'] = '01.0eM' # or: ('1em', 'important')

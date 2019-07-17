import cssutils 
import webcolors 

sheet = cssutils.parseFile('main.css')

# def main(): 
#     f= open("newer_css.css", "a+") 
    
for rule in sheet: 
    if rule.type == rule.STYLE_RULE: 
        # find property 
        for property in rule.style:
            if property.name == 'color':
                if property.value != 'inherit': 
                    if property.value[0] != "#": 
                        property.value = webcolors.CSS3_NAMES_TO_HEX[property.value]
                # property.priority = 'IMPORTANT'


# new = cssutils.parseFile(sheet.cssText)
print(sheet.cssText)
# print(new) 


# Write to a new file
with open('test_css.css', 'wb') as f:
    f.write(sheet.cssText)



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

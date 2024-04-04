# *************************** Importing required libararies ************************
import json 
import pycountry
from tkinter import Tk, Label, Button, Entry
from phone_iso3166.country import phone_country


# ****************************** Function *************************************
class Location_Tracker:
    def __init__(self, App):
        self.window = App
        self.window.title("Phone Number Tracker Application")
        self.window.geometry("540x400")
        self.window.configure(bg="#3f5efb")
        self.window.resizable(False, False)

        # ********************* App manu *************************************
        Label(App, text="Plese! Enter the phone number with country code", fg="white", font=("Times", 18), bg="#3f5efb").place(x=25, y=30)
        self.phone_number = Entry(App, width=16, font=("Arial", 15), relief="flat", bd=5)
        self.track_button = Button(App, text="Click here", bg="#22c1c3", relief="sunken", cursor="hand2")
        self.country_label = Label(App, fg="white", font=("Times", 18), bg="#3f5efb"); 

        # ******************** window pop up page ****************************
        self.phone_number.place(x=170, y=120)
        self.track_button.place(x=200, y=200)
        self.country_label.place(x=100, y=280)

        # ********************* countries buttons ****************************
        self.track_button.bind("<Button-1>", self.Track_location)
        
    
    # ************************* Location Tracking function *******************
    def Track_location(self, event):
        phone_number = self.phone_number.get()
        country = "Country is Unknown"
        if phone_number:
            try:
                country_code = phone_country(phone_number)
                tracked = pycountry.countries.get(alpha_2=country_code)
                print(tracked)
                if tracked:
                    if hasattr(tracked, "official_name"):
                        country = tracked.official_name
                    else:
                        country = tracked.name
            # *************** Generic exception catch ************************           
            except Exception as e:
                country = "Invalid input or country not found."
        self.country_label.configure(text=country)

# ************************** Function calls **********************************
PhoneTracker = Tk()
MyApp = Location_Tracker(PhoneTracker)
PhoneTracker.mainloop()
# def menu():
#     print("List of menu functions")
#     print(f'''
#     1.Phone book
#     2.Messages
#     3.Chat
#     4.Call register
#     5.Tones
#     6.Settings
#     7.Call divert
#     8.Games
#     9.Calculator
#     10.Remainder
#     11.Clock
#     12.Profile
#     13.Sim services
#     ''')
#     user_input = input('Enter a number: ')
#     match user_input:
#         case '1':
#             (
#                 phone_book())
#         case '2':
#             (
#                 messages())
#         case '3':
#             (
#                 chat())
#         case '4':
#             (
#                 call_register())
#         case '5':
#             (
#                 tones())
#         case '6':
#             (
#                 setting())
#         case '7':
#             (
#                 call_divert())
#         case '8':
#             (
#                 games())
#         case '9':
#             (
#                 calculator())
#         case '10':
#             (
#                 reminder())
#         case '11':
#             (
#                 clock())
#         case '12':
#             (
#                 profile())
#         case '13':
#             (
#                 sim_services())
#         case _:
#             (
#                 menu())
#
#
# def phone_book():
#     print("Phone book")
#     print(f'''
#         1.Search
#         2.Services Nos
#         3.Add name
#         4.Erase
#         5.Edit
#         6.Assign tone
#         7.Send b'card
#         8.Option
#         9.Speed dials
#         10.Voice tags
#         ''')
#     user_input = input('Enter a number or press 0 to go back: ')
#     if user_input == '8':
#         option()
#     elif user_input == '0':
#         return menu()
#     else:
#         print('invalid command', phone_book())
#
#
# def option():
#     print("Option")
#     print(f'''
#     1.Type of view
#     2.Memory status
#     ''')
#     user_input = input('Enter a number or press 0 to go back: ')
#     if user_input == '1':
#         type_of_view()
#     elif user_input == '2':
#         memory_status()
#     elif user_input == '0':
#         return phone_book()
#     else:
#         print('invalid command', option())
#
#
# def type_of_view():
#     print("Types of view")
#     user_input = input('Enter press 0 to go back: ')
#     if user_input == '0':
#         option()
#
#
# def memory_status():
#     print("Memory status")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         option()
#
#
# def messages():
#     print("Messages")
#     print(f'''
#     1.Write messages
#     2.Inbox
#     3.Outbox
#     4.Picture messages
#     5.Templates
#     6.Smileys
#     7.Messages settings
#     8.Info service
#     9.Voice mailbox numbers
#     10.Service command editor
#     ''')
#     user_input = input('Enter a number or press 0 to go back: ')
#     if user_input == '7':
#         messages_settings()
#     elif user_input == '0':
#         return menu()
#     else:
#         print('invalid command', messages())
#
#
# def messages_settings():
#     print("Messages setting")
#     print(f'''
#     1.Set1
#     2.Common3
#     ''')
#     user_input = input('Enter a number or press 0 to go back: ')
#     if user_input == '1':
#         set1()
#     elif user_input == '2':
#         common3()
#     else:
#         print('invalid command', messages_settings())
#
#
# def set1():
#     print("Set1")
#     print(f'''
#     1.Messages center number
#     2.Message sent as
#     3.Message validity
#     ''')
#     user_input = input('Enter a number or press 0 to go back: ')
#     if user_input == '1':
#         message_center_number()
#     elif user_input == '2':
#         message_sent_as()
#     elif user_input == '3':
#         message_validity()
#     elif user_input == '0':
#         return messages()
#     else:
#         print('invalid command', messages_settings())
#
#
# def message_center_number():
#     print("Message centre number")
#     user_input = input('Enter 0 to go back:  ')
#     if user_input == '0':
#         set1()
#
#
# def message_sent_as():
#     print("Message sent as")
#     user_input = input('Enter 0 to go back:  ')
#     if user_input == '0':
#         set1()
#
#
# def message_validity():
#     print("Message validity")
#     user_input = input('Enter 0 to go back:  ')
#     if user_input == '0':
#         set1()
#
#
# def common3():
#     print("Common 3")
#     print(f'''
#     1.Delivery reports
#     2.Reply via same centre
#     3.Character support
#     ''')
#
#     user_input = input("Enter a number or press 0 to go back: ")
#     if user_input == '1':
#         return delivery_report()
#     elif user_input == '2':
#         return reply_via_same_center()
#     elif user_input == '3':
#         return character_support()
#     elif user_input == '0':
#         return messages()
#     else:
#         print('invalid command', messages_settings())
#
#
# def delivery_report():
#     print("DeliverY reports")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         common3()
#
#
# def reply_via_same_center():
#     print('Reply via same centre')
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         common3()
#
#
# def character_support():
#     print("Character support")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         common3()
#
#
# def chat():
#     print("Character support")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         return menu()
#
#
# def call_register():
#     print("Call register")
#     print(f'''
#     1.Missed calls
#     2.Received calls
#     3.Dialled numbers
#     4.Erase recent call lists
#     5.Show call duration
#     6.Show call costs
#     7.Call cost settings
#     8.Prepaid credit
#     ''')
#     user_input = input("Enter a number or press 0 to go back: ")
#     if user_input == '5':
#         return show_call_duration()
#     elif user_input == '6':
#         return show_call_cost()
#     elif user_input == '7':
#         return call_cost_setting()
#     elif user_input == '0':
#         return menu()
#     else:
#         print('invalid command', call_register())
#
#
# def show_call_duration():
#     print("Show call duration")
#     print(f'''
#     1.Last call duration
#     2.All calls' duration
#     3.Received calls' duration
#     4.Dialled calls' duration
#     5.Clear timers
#     ''')
#     user_input = input("Enter a number or press 0 to go back: ")
#     if user_input == '1':
#         return last_call_duration()
#     elif user_input == '2':
#         return all_calls_duration()
#     elif user_input == '3':
#         return received_calls_duration()
#     elif user_input == '4':
#         dialled_calls_duration()
#     elif user_input == '5':
#         return clear_timers()
#     elif user_input == '0':
#         return menu()
#     else:
#         print('invalid command', show_call_duration())
#
#
# def last_call_duration():
#     print("Last call duration")
#     user_input = input("Enter a number or press 0 to go back: ")
#     if user_input == '0':
#         show_call_duration()
#
#
# def all_calls_duration():
#     print("All calls' duration")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         show_call_duration()
#
#
# def received_calls_duration():
#     print("Received calls' duration")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         show_call_duration()
#
#
# def dialled_calls_duration():
#     print("Dialled calls' duration")
#     user_input = input("Enter a number or press 0 to go back: ")
#     if user_input == '0':
#         show_call_duration()
#
#
# def clear_timers():
#     print("Clear timers")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         show_call_duration()
#
#
# def show_call_cost():
#     print("Show call costs")
#     print(f'''
#     1.Last call cost
#     2.All calls' cost
#     3.Clear counters
#     ''')
#     user_input = input("Enter a number or press 0 to go back: ")
#     if user_input == '1':
#         last_call_cost()
#     elif user_input == '2':
#         all_calls_cost()
#     elif user_input == '3':
#         clear_counters()
#     elif user_input == '0':
#         return menu()
#     else:
#         print('invalid command', show_call_cost())
#
#
# def last_call_cost():
#     print("Last call cost")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         show_call_cost()
#
#
# def all_calls_cost():
#     print("All calls' cost")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         show_call_cost()
#
#
# def clear_counters():
#     print("Clear counters")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         show_call_cost()
#
#
# def call_cost_setting():
#     print("Call cost setting")
#     print(f'''
#     1.Call cost limit
#     2.Show cost in
#     ''')
#     user_input = input("Enter a number or press 0 to go back: ")
#     if user_input == '1':
#         call_cost_limit()
#     elif user_input == '2':
#         show_cost_in()
#     elif user_input == '0':
#         return menu()
#     else:
#         print('invalid command', call_cost_setting())
#
#
# def call_cost_limit():
#     print("Call cost limit")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         call_cost_setting()
#
#
# def show_cost_in():
#     print("Show costs in")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         call_cost_setting()
#
#
# def tones():
#     print("Tones")
#     print(f'''
#     1.Ringing tone
#     2.Ringing volume
#     3.Incoming call alert
#     4.Composer
#     5.Message alert tone
#     6.Keypad tones
#     7.Warming and game tones
#     8.Vibrating alert
#     9.Screen saver
#     ''')
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         return menu()
#
#
# def setting():
#     print("Settings")
#     print(f'''
#     1.Call settings
#     2.Phone settings
#     3.Security settings
#     4.Restore factory settings
#     ''')
#     user_input = input("Enter a number or press 0 to go back: ")
#     if user_input == '1':
#         call_settings()
#     elif user_input == '2':
#         phone_settings()
#     elif user_input == '3':
#         security_settings()
#     elif user_input == '4':
#         restore_factory_settings()
#     elif user_input == '0':
#         return menu()
#     else:
#         print('invalid command', setting())
#
#
# def call_settings():
#     print("Call settings")
#     print(f'''
#     1.Automatic redial
#     2.Speed dialling
#     3.Call waiting options
#     4.Own number sending
#     5.Phone line in use
#     6.Automatic answer
#     ''')
#     user_input = input("Enter a number or press 0 to go back: ")
#     if user_input == '1':
#         automatic_redial()
#     elif user_input == '2':
#         speed_dialling()
#     elif user_input == '3':
#         call_waiting_options()
#     elif user_input == '4':
#         own_number_sending()
#     elif user_input == '5':
#         phone_line_in_use()
#     elif user_input == '6':
#         automatic_answer()
#     elif user_input == '0':
#         return setting()
#     else:
#         print('invalid command', call_settings())
#
#
# def automatic_redial():
#     print("Automatic Redial")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         call_settings()
#
#
# def speed_dialling():
#     print("Speed dialling")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         call_settings()
#
#
# def call_waiting_options():
#     print("Call waiting options")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         call_settings()
#
#
# def own_number_sending():
#     print("Own number sending")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         call_settings()
#
#
# def phone_line_in_use():
#     print("Phone line in use")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         call_settings()
#
#
# def automatic_answer():
#     print("Automatic answer")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         call_settings()
#
#
# def phone_settings():
#     print("Phone settings")
#     print(f'''
#     1.Language
#     2.Cell info display
#     3.Welcome note
#     4.Network selection
#     5.Light
#     6.Confirm sim services actions
#     '''
#           )
#     user_input = input("Enter a number or press 0 to go back: ")
#     if user_input == '1':
#         language()
#     elif user_input == '2':
#         cell_info_display()
#     elif user_input == '3':
#         welcome_note()
#     elif user_input == '4':
#         network_selection()
#     elif user_input == '5':
#         light()
#     elif user_input == '6':
#         confirm_sim_service_actions()
#     elif user_input == '0':
#         return setting()
#     else:
#         print('invalid command', phone_settings())
#
#
# def language():
#     print("Language")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         phone_settings()
#
#
# def cell_info_display():
#     print("Cell info display")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         phone_settings()
#
#
# def welcome_note():
#     print("Welcome note")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         phone_settings()
#
#
# def network_selection():
#     print("Network selection")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         phone_settings()
#
#
# def light():
#     print("Lights")
#     user_input = input('Enter press 0 to go back: ')
#     if user_input == '0':
#         phone_settings()
#
#
# def confirm_sim_service_actions():
#     print("Confirm Sim service actions")
#     user_input = input('Enter press 0 to go back: ')
#     if user_input == '0':
#         phone_settings()
#
#
# def security_settings():
#     print("Security settings")
#     print(f'''
#     1.Pin code request
#     2.Call barring service
#     3.Fixed dialling
#     4.Closed user group
#     5.Phone security
#     6.Change access codes
#     '''
#           )
#     user_input = input('Enter a number or press 0 to go back: ')
#     if user_input == '1':
#         pin_code_request()
#     elif user_input == '2':
#         call_barring_service()
#     elif user_input == '3':
#         fixed_dialling()
#     elif user_input == '4':
#         closed_user_group()
#     elif user_input == '5':
#         phone_security()
#     elif user_input == '6':
#         change_access_codes()
#     elif user_input == '0':
#         return setting()
#     else:
#         print('invalid command', security_settings())
#
#
# def pin_code_request():
#     print("Pin code request")
#     user_input = input('Enter press 0 to go back: ')
#     if user_input == '0':
#         security_settings()
#
#
# def call_barring_service():
#     print("Call barring service")
#     user_input = input('Enter press 0 to go back: ')
#     if user_input == '0':
#         security_settings()
#
#
# def fixed_dialling():
#     print("Fixed dialling")
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         security_settings()
#
#
# def closed_user_group():
#     print("Closed user group")
#     user_input = int(input('Enter press 0 to go back: '))
#     if user_input == '0':
#         security_settings()
#
#
# def phone_security():
#     print("Phone security")
#     user_input = input('Enter press 0 to go back: ')
#     if user_input == '0':
#         security_settings()
#
#
# def change_access_codes():
#     print("Change access codes")
#     user_input = input('Enter press 0 to go back: ')
#     if user_input == '0':
#         security_settings()
#
#
# def restore_factory_settings():
#     print("Restore factory settings")
#     user_input = input('Enter press 0 to go back: ')
#     if user_input == '0':
#         return menu()
#     else:
#         print('invalid command', setting())
#
#
# def call_divert():
#     print('Call divert')
#     user_input = input('Enter press 0 to go back: ')
#     if user_input == '0':
#         menu()
#
#
# def games():
#     print('Games')
#     user_input = input('Enter press 0 to go back: ')
#     if user_input == '0':
#         return menu()
#
#
# def addition():
#     pass
#
#
# def subtraction():
#     pass
#
#
# def multiplication():
#     pass
#
#
# def calculator():
#     print('Calculator')
#     print(
#         f'''
#         1.Addition
#         2.Subtraction
#         3.Multiplication
#         3.Division''')
#     user_input = input('Enter a number to calculate_input: ')
#     if user_input == "1":
#         addition()
#     elif user_input == "2":
#         subtraction()
#     elif user_input == "3":
#         multiplication()
#     elif user_input == "4":
#         division()
#
#
#
# def reminder():
#     print('Reminder')
#     user_input = input('Enter press 0 to go back: ')
#     if user_input == '0':
#         return menu()
#
#
# def clock():
#     print('Clock')
#     print(f'''
#     1.Alarm clock
#     2.Clock settings
#     3.Date setting
#     4.Stopwatch
#     5.Countdown timer
#     6.Auto update of date and time
#     ''')
#     user_input = input('Enter press 0 to go back: ')
#     if user_input == '0':
#         return menu()
#
#
# def profile():
#     print('Profile')
#     user_input = input('Enter press 0 to go back: ')
#     if user_input == '0':
#         return menu()
#
#
# def sim_services():
#     print('Sim services')
#     user_input = input("Enter press 0 to go back: ")
#     if user_input == '0':
#         return menu()
#
#
# menu()
#

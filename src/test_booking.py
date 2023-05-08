# import pytest 
# import csv 
# from io import StringIO 
# from booking import display_bookings

# # # assertion
# # def test_display_bookings():
# #     test_date = StringIO()
# #     booking_files = "test_bookings.csv"
# #     with open("test_bookings.csv", mode="w") as csvfile:
# #         writer = csv.writer(csvfile)
# #         writer.writerow(["ABC", "A", "100", "1", "2023-05-08"])
        

# #     # call the function with the test data
# #     csvfile.seek(0)
# #     with open("test_bookings.csv", mode="w") as csvfile:
# #         csvfile.write(test_data.read())
        
# #     # check output
# #     sys.stdout = sys.__stdout__
    
# #     expected_output = "User: ABC", "Room Choice: A", "Total Cost: 100", "Number of Nights: 1", "Booking date: 2023-05-08"
# #     assert expected_output == output.getvalue()
# def test_display_bookings():
#       with open("test_bookings.csv", mode="r") as csvfile:
#         reader = csv.reader(csvfile)
#         # Skip the header row
#         next(reader)
#         # Count the remaining rows
#         row_count = sum(1 for row in reader)

#     # Assert that the row count is correct
#     assert row_count == 5
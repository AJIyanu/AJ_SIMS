
import moment from "moment-timezone";

const table =  [
    {
        "invoiceNumber": 300500,
        "status": "Paid",
        "subscription": "Platinum Subscription Plan",
        "price": "799,00",
        "issueDate": moment().subtract(1, "days").format("DD MMM YYYY"),
        "dueDate": moment().subtract(1, "days").add(1, "month").format("DD MMM YYYY")
    },
    {
        "invoiceNumber": 300499,
        "status": "Paid",
        "subscription": "Platinum Subscription Plan",
        "price": "799,00",
        "issueDate": moment().subtract(2, "days").format("DD MMM YYYY"),
        "dueDate": moment().subtract(2, "days").add(1, "month").format("DD MMM YYYY")
    },
    {
        "invoiceNumber": 300498,
        "status": "Paid",
        "subscription": "Platinum Subscription Plan",
        "price": "799,00",
        "issueDate": moment().subtract(2, "days").format("DD MMM YYYY"),
        "dueDate": moment().subtract(2, "days").add(1, "month").format("DD MMM YYYY")
    },
    {
        "invoiceNumber": 300497,
        "status": "Paid",
        "subscription": "Flexible Subscription Plan",
        "price": "233,42",
        "issueDate": moment().subtract(3, "days").format("DD MMM YYYY"),
        "dueDate": moment().subtract(3, "days").add(1, "month").format("DD MMM YYYY")
    },
    {
        "invoiceNumber": 300496,
        "status": "Due",
        "subscription": "Gold Subscription Plan",
        "price": "533,42",
        "issueDate": moment().subtract(1, "day").subtract(1, "month").format("DD MMM YYYY"),
        "dueDate": moment().subtract(1, "day").format("DD MMM YYYY")
    },
    {
        "invoiceNumber": 300495,
        "status": "Due",
        "subscription": "Gold Subscription Plan",
        "price": "533,42",
        "issueDate": moment().subtract(3, "days").subtract(1, "month").format("DD MMM YYYY"),
        "dueDate": moment().subtract(3, "days").format("DD MMM YYYY")
    },
    {
        "invoiceNumber": 300494,
        "status": "Due",
        "subscription": "Flexible Subscription Plan",
        "price": "233,42",
        "issueDate": moment().subtract(4, "days").subtract(1, "month").format("DD MMM YYYY"),
        "dueDate": moment().subtract(4, "days").format("DD MMM YYYY")
    },
    {
        "invoiceNumber": 300493,
        "status": "Canceled",
        "subscription": "Gold Subscription Plan",
        "price": "533,42",
        "issueDate": moment().subtract(20, "days").subtract(1, "month").format("DD MMM YYYY"),
        "dueDate": moment().subtract(20, "days").format("DD MMM YYYY")
    },
    {
        "invoiceNumber": 300492,
        "status": "Canceled",
        "subscription": "Platinum Subscription Plan",
        "price": "799,00",
        "issueDate": moment().subtract(2, "months").format("DD MMM YYYY"),
        "dueDate": moment().subtract(3, "months").format("DD MMM YYYY")
    },
    {
        "invoiceNumber": 300491,
        "status": "Paid",
        "subscription": "Platinum Subscription Plan",
        "price": "799,00",
        "issueDate": moment().subtract(6, "days").format("DD MMM YYYY"),
        "dueDate": moment().subtract(6, "days").add(1, "month").format("DD MMM YYYY")
    }
]

export default [
    {
        "Subject": "Mathematics",
        "Code": "MTH102",
        "Attendance": "100%",
        "Assignment": 8,
        "CA_Test": 19,
        "Exam": 50,
        "Total": 87,
        "Position": "2nd"
    },
    {
        "Subject": "English",
        "Code": "ENG102",
        "Attendance": "100%",
        "Assignment": 6,
        "CA_Test": 14,
        "Exam": 50,
        "Total": 87,
        "Position": "2nd"
    },
    {
        "Subject": "Biology",
        "Code": "BIO102",
        "Attendance": "100%",
        "Assignment": 8,
        "CA_Test": 19,
        "Exam": 50,
        "Total": 87,
        "Position": "2nd"
    },
    {
        "Subject": "Physics",
        "Code": "PHY102",
        "Attendance": "100%",
        "Assignment": 8,
        "CA_Test": 19,
        "Exam": 50,
        "Total": 87,
        "Position": "2nd"
    },
    {
        "Subject": "Chemistry",
        "Code": "CHM102",
        "Attendance": "100%",
        "Assignment": 8,
        "CA_Test": 19,
        "Exam": 50,
        "Total": 87,
        "Position": "2nd"
    },
    {
        "Subject": "Yoruba",
        "Code": "YOR102",
        "Attendance": "100%",
        "Assignment": 8,
        "CA_Test": 19,
        "Exam": 50,
        "Total": 87,
        "Position": "2nd"
    },
    {
        "Subject": "Geography",
        "Code": "GEO102",
        "Attendance": "100%",
        "Assignment": 8,
        "CA_Test": 19,
        "Exam": 50,
        "Total": 87,
        "Position": "2nd"
    }
]

# Tables in Resume APP

User
    -id
    -username

Personal details
    -id
    -name
    -phone
    -email
    -address
    -linkedin_url1
    -Foreign_key("user_id")

Experience
    -id
    -company_name
    -role
    -role_desc
    -start_date
    -end_date

certificate
    -id
    -title
    -start_date
    -end_date

eduction
    -id
    school_name
    -degree_name
    -start_date
    -end_date
    ForeignKey('user_id')

skills
    -id
    -title
    -confidence score
    -ForeignKey('user_id')

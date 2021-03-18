from flask_restx import Namespace, fields

class ResumeDto:
    api = Namespace('resume', description='resume related operations')
    resume = api.model('resume', {
        'id': fields.String(description='resume id'),
        'job': fields.String(description='job applied for'),
        'company': fields.String(description='hiring company'),
        'contact': fields.String(description='person or people that are in contact'),
        'phone': fields.String(description='phone number for contact'),
        'comms': fields.String(description='email or other contact methods'),
        'address': fields.String(description='mailing address of company'),
        'website': fields.String(description='company website'),
        'date_submitted': fields.String(description='date resume submitted'),
        'cover_letter_date': fields.String(description='date cover letter submitted'),
        'references': fields.String(description='references sent'),
        'discovered_by': fields.String(description='how you heard of this job'),
        'job_description': fields.String(description='job description and keywords'),
        'status': fields.String(description='status of application'),
        'comments': fields.String(description='comments and/or notes on this application')
    })

class InterviewDto:
    api = Namespace('interview', description='interview related operations')
    interview = api.model('interview', {
        'id': fields.String(description='interview id'),
        'date': fields.String(description='date of interview'),
        'interviewer': fields.String(description='interviewer name and title'),
        'phone': fields.String(description='phone number'),
        'comms': fields.String(description='email and other contact'),
        'interview_address': fields.String(description='address of interview'),
        'mailing_address': fields.String(description='mailing address of company'),
        'follow_up_date': fields.String(description='date thank you letter or other inquiries sent'),
        'comments': fields.String(description='comments and notes on interview and other info')
    })

class NetworkDto:
    api = Namespace('network', description='networking related operations')
    network = api.model('network', {
        'id': fields.String(description='networking id'),
        'acquaintance': fields.String(description='acquaintance name and title'),
        'company': fields.String(description='company name'),
        'comms': fields.String(description='contact information'),
        'comments': fields.String(description='comments on acquaintance')
    })

class LeadDto:
    api = Namespace('lead', description='lead related operations')
    lead = api.model('lead', {
        'id': fields.String(description='lead id'),
        'name': fields.String(description='lead name and title'),
        'company': fields.String(description='company lead works for'),
        'comms': fields.String(description='contact information'),
        'comments': fields.String(description='comments and notes on lead')
    })

class WebsiteDto:
    api = Namespace('website', description='website related operations')
    website = api.model('website', {
        'id': fields.String(description='website id'),
        'website': fields.String(description='website'),
        'username': fields.String(description='username used on website'),
        'resume_date': fields.String(description='date resume posted'),
        'cover_letter_date': fields.String(description='date cover letter posted'),
        'comments': fields.String(description='comments and notes on website')
    })
import LogoFacebook from '@/components/Icons/FacebookIcon.vue'
import LogoInstagram from '@/components/Icons/InstagramIcon.vue'
import LogoWhatsApp from '@/components/Icons/WhatsAppIcon.vue'

export const supportedSourceTypes = [
  {
    label: 'Facebook',
    value: 'Facebook',
    icon: LogoFacebook,
    info: __(
      'You will need a Meta developer account and an access token to sync leads from Facebook. Read more',
    ),
    link: 'https://www.facebook.com/business/help/503306463479099?id=2190812977867143',
    custom: false,
  },
  {
    label: 'Instagram',
    value: 'Instagram',
    icon: LogoInstagram,
    info: __(
      'Instagram Lead Ads use the same Meta API as Facebook. You will need a Meta developer account and an access token. Read more',
    ),
    link: 'https://www.facebook.com/business/help/503306463479099?id=2190812977867143',
    custom: false,
  },
  {
    label: 'WhatsApp',
    value: 'WhatsApp',
    icon: LogoWhatsApp,
    info: __(
      'Leads are automatically created from incoming WhatsApp messages from new contacts.',
    ),
    link: '',
    custom: false,
  },
]

export const sourceIcon = {
  Facebook: LogoFacebook,
  Instagram: LogoInstagram,
  WhatsApp: LogoWhatsApp,
}

export const fbSourceFields = [
  {
    name: 'name',
    label: __('Name'),
    type: 'text',
    placeholder: __('Add a name for your source'),
  },
  {
    name: 'access_token',
    label: __('Access Token'),
    type: 'password',
    placeholder: __('Enter your Facebook Access Token'),
  },
]

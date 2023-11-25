from django.contrib.sites import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import requests

@csrf_exempt
@require_http_methods(["POST"])
def receive_string(request):
    global json_response, scores
    received_str = request.POST.get('string_data', None)
    print(received_str)

    # https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url
    # =https://developers.google.com&strategy=desktop&category=performance

    # api_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'
    # response = request.get(api_url, data={'url': received_str, 'strategy': 'desktop', 'category=performance': 'perfomance'})
    # json_response = response.json()

    if received_str:
        api_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'
        params = {
            'url': received_str,
            'strategy': 'desktop',
            # 'category': 'accessibility'
            'category': ['performance', 'accessibility', 'best-practices', 'seo']
        }
        response = requests.get(api_url, params=params)  # використання requests.get замість request.get
        json_response = response.json()


        performance_score = json_response['lighthouseResult']['categories']['performance']['score'] * 100
        accessibility_score = json_response['lighthouseResult']['categories']['accessibility']['score'] * 100
        best_practices_score = json_response['lighthouseResult']['categories']['best-practices']['score'] * 100
        seo_score = json_response['lighthouseResult']['categories']['seo']['score'] * 100

        print(f"Performance: {performance_score}")
        print(f"Accessibility: {accessibility_score}")
        print(f"Best Practices: {best_practices_score}")
        print(f"SEO: {seo_score}")

        scores = {
            'performance_score': performance_score,
            'accessibility_score': accessibility_score,
            'best_practices_score': best_practices_score,
            'seo_score': seo_score
        }

    # if received_str is not None:
    #     return JsonResponse({'status': 'success', 'received_str': received_str})
    # else:
    #     return JsonResponse({'status': 'error', 'message': 'No string provided'})
    if received_str is not None:
        return render(request, 'input_form.html', {'json_response': json_response, 'scores': scores})
    else:
        return JsonResponse({'status': 'error', 'message': 'No string provided'})

def input_form(request):
    if request.method == 'GET':
        return render(request, 'input_form.html')

@require_http_methods(["GET"])
def api_view(request):
    global result_data
    url_to_analyze = request.GET.get('url', None)
    comment = request.GET.get('comment', '')

    if url_to_analyze:
        api_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'
        params = {
            'url': url_to_analyze,
            'strategy': 'desktop',
            'category': ['performance', 'accessibility', 'best-practices', 'seo']
        }
        response = requests.get(api_url, params=params)
        json_response = response.json()

        scores = {
            'performance_score': json_response['lighthouseResult']['categories']['performance']['score'] * 100,
            'accessibility_score': json_response['lighthouseResult']['categories']['accessibility']['score'] * 100,
            'best_practices_score': json_response['lighthouseResult']['categories']['best-practices']['score'] * 100,
            'seo_score': json_response['lighthouseResult']['categories']['seo']['score'] * 100
        }

        all_audits = json_response['lighthouseResult']['audits']
        audits_data = {}

        for audit_id, audit_info in all_audits.items():
            audits_data[audit_id] = {
                'title': audit_info['title'],
                'description': audit_info.get('description', ''),
                'score': audit_info.get('score', None),
                'displayValue': audit_info.get('displayValue', '')
            }

        opportunities = json_response['lighthouseResult']['audits']
        opportunities_data = {}

        for audit_name, audit_details in opportunities.items():
            if audit_details.get('score') is not None and audit_details.get('score') < 1:
                if 'details' in audit_details and audit_details['details'].get('type') == 'opportunity':
                    opportunities_data[audit_name] = {
                        'title': audit_details.get('title'),
                        'description': audit_details.get('description'),
                        'score': audit_details.get('score'),
                        'displayValue': audit_details['details'].get('displayValue', 'No display value'),
                    }

            result_data = {
                'scores': scores,
                # 'audits': audits_data
                'opportunities_data': opportunities_data,
            }

        return JsonResponse(result_data)
    else:
        return JsonResponse({'error': 'URL parameter is missing.'})

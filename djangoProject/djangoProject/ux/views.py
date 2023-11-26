from django.contrib.sites import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.templatetags.static import static
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


@require_http_methods(['GET'])
def api_chat(request):
    url = request.GET.get('url', None)

    # https://www.alza.sk/

    target_url = 'https://www.alza.sk/'

    if url == target_url:
        response_data = [
            {
                'id': 1,
                'title': 'Black Friday Deals at Alza',
                'img': "https://i.imgur.com/uFlLgXV.png",
                'pros': [
                    'Brand Consistency: The use of a green color scheme and the mascot is consistent with the branding, which helps in brand recall.',
                    'Clear Hierarchy: The navigation menu on the left is clearly visible and well organized, aiding in user navigation.',
                    'Prominent Search Bar: The search bar is in a prime location and easily accessible, which is good for user experience.',
                ],
                'cons': [
                    'Information Overload: There\'s a lot going on visually with multiple promotions and banners fighting for attention, which can overwhelm the user.',
                    'Consistency in Design: The variety of banner sizes and styles (some with characters, others with products, different backgrounds, etc.) makes the page feel a little disjointed. A more cohesive look could improve navigation.',
                    'Use of Space: There is a lot of information packed into the viewport, and it might benefit from more white space to help each section stand out and reduce the sense of clutter.',
                    'Visual Priority: The main deals should have clear visual dominance, but the current layout doesn\'t strongly guide the eye to the most critical areas or intended user paths.',
                    'Call-to-Action Buttons: Some CTAs, like "Viac" on the promotional banners, could be more pronounced to better draw user interaction.',
                    'Advertisement Clarity: It\'s not immediately clear which items are advertisements and which are navigational elements',
                ],
                'problems': 6,
            },
            {
                'id': 2,
                'title': 'Shopping Cart Summary',
                'img': 'https://i.imgur.com/jK0Xx9X.png',
                'pros': [
                    'Clear Step Indicator: The checkout process is broken down into steps (basket, shipping and payment, delivery details), which is a good practice for letting users know where they are in the process.',
                    'Product Visibility: The image, name, and price of the product is clearly visible which helps users to confirm they have the correct item in their cart.',
                    'Call to Action (CTA) Visibility: The “Continue” button is a contrasting color, making it highly visible and guiding the user towards the next step.',
                    'Option to Enter Promo Codes: There is a clear option to enter discount codes, which is good for customer engagement.',
                ],
                'cons': [
                    'Information Density: There is a lot of information presented in a small area which can feel cluttered. Simplifying and spacing out this information could help readability.',
                    'Upsell Items: While it is a good practice to recommend additional items, the suggestions lack context and are not immediately clear how they relate to the item in the cart.',
                    'Visual Hierarchy: The visibility of secondary buttons such as "Back to shopping" or service guarantees could be improved by differentiating them more from the main CTA.',
                    'Cart Edit Options: It should be made clearer how users can change the quantity or remove items directly from the cart page',
                ],
                'problems': 4,
            },
            {
                'id': 3,
                'title': 'Choose Your Delivery Option',
                'img': 'https://i.imgur.com/dIuiJem.png',
                'problems': 3,
            },
            {
                'id': 4,
                'title': 'Select Payment Method',
                'img': 'https://i.imgur.com/JGvPT6C.png',
                'problems': 3,
            },
            {
                'id': 5,
                'title': 'Checkout Login Options',
                'img': 'https://i.imgur.com/Kw52Ood.png',
                'problems': 2,
            },
            {
                'id': 6,
                'title': 'Track Your Order Status',
                'img': 'https://i.imgur.com/OXoSTO4.png',
                'problems': 2,
            },
            {
                'id': 7,
                'title': 'Your Account Overview',
                'img': 'https://i.imgur.com/CSOe1Eb.png',
                'problems': 2,
            }
        ]

        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({'error': 'URL parameter is missing.'})

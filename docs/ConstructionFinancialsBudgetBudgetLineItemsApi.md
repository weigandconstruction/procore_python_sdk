# procore_sdk.ConstructionFinancialsBudgetBudgetLineItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_budget_line_items_id_get**](ConstructionFinancialsBudgetBudgetLineItemsApi.md#rest_v10_budget_line_items_id_get) | **GET** /rest/v1.0/budget_line_items/{id} | Show Budget Line Item
[**rest_v10_budget_line_items_id_patch**](ConstructionFinancialsBudgetBudgetLineItemsApi.md#rest_v10_budget_line_items_id_patch) | **PATCH** /rest/v1.0/budget_line_items/{id} | Update Budget Line Item
[**rest_v10_budget_line_items_post**](ConstructionFinancialsBudgetBudgetLineItemsApi.md#rest_v10_budget_line_items_post) | **POST** /rest/v1.0/budget_line_items | Create Budget Line Item
[**rest_v10_budget_line_items_sync_post**](ConstructionFinancialsBudgetBudgetLineItemsApi.md#rest_v10_budget_line_items_sync_post) | **POST** /rest/v1.0/budget_line_items/sync | Sync Budget Line Items
[**rest_v11_budget_line_items_id_get**](ConstructionFinancialsBudgetBudgetLineItemsApi.md#rest_v11_budget_line_items_id_get) | **GET** /rest/v1.1/budget_line_items/{id} | Show Budget Line Item
[**rest_v11_budget_line_items_id_patch**](ConstructionFinancialsBudgetBudgetLineItemsApi.md#rest_v11_budget_line_items_id_patch) | **PATCH** /rest/v1.1/budget_line_items/{id} | Update Budget Line Item
[**rest_v11_budget_line_items_post**](ConstructionFinancialsBudgetBudgetLineItemsApi.md#rest_v11_budget_line_items_post) | **POST** /rest/v1.1/budget_line_items | Create Budget Line Item


# **rest_v10_budget_line_items_id_get**
> RestV10BudgetLineItemsPost201Response rest_v10_budget_line_items_id_get(procore_company_id, id, project_id)

Show Budget Line Item

Return information about a Budget Line Item.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_budget_line_items_post201_response import RestV10BudgetLineItemsPost201Response
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Budget Line Item
        api_response = api_instance.rest_v10_budget_line_items_id_get(procore_company_id, id, project_id)
        print("The response of ConstructionFinancialsBudgetBudgetLineItemsApi->rest_v10_budget_line_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetLineItemsApi->rest_v10_budget_line_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10BudgetLineItemsPost201Response**](RestV10BudgetLineItemsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_budget_line_items_id_patch**
> RestV10BudgetLineItemsPost201Response rest_v10_budget_line_items_id_patch(procore_company_id, id, body119)

Update Budget Line Item

Update a line item of a specified budget.

### Example


```python
import procore_sdk
from procore_sdk.models.body119 import Body119
from procore_sdk.models.rest_v10_budget_line_items_post201_response import RestV10BudgetLineItemsPost201Response
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    body119 = procore_sdk.Body119() # Body119 | 

    try:
        # Update Budget Line Item
        api_response = api_instance.rest_v10_budget_line_items_id_patch(procore_company_id, id, body119)
        print("The response of ConstructionFinancialsBudgetBudgetLineItemsApi->rest_v10_budget_line_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetLineItemsApi->rest_v10_budget_line_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **body119** | [**Body119**](Body119.md)|  | 

### Return type

[**RestV10BudgetLineItemsPost201Response**](RestV10BudgetLineItemsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Currency |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_budget_line_items_post**
> RestV10BudgetLineItemsPost201Response rest_v10_budget_line_items_post(procore_company_id, body118)

Create Budget Line Item

Add a new line item to a budget.

### Example


```python
import procore_sdk
from procore_sdk.models.body118 import Body118
from procore_sdk.models.rest_v10_budget_line_items_post201_response import RestV10BudgetLineItemsPost201Response
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body118 = procore_sdk.Body118() # Body118 | 

    try:
        # Create Budget Line Item
        api_response = api_instance.rest_v10_budget_line_items_post(procore_company_id, body118)
        print("The response of ConstructionFinancialsBudgetBudgetLineItemsApi->rest_v10_budget_line_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetLineItemsApi->rest_v10_budget_line_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body118** | [**Body118**](Body118.md)|  | 

### Return type

[**RestV10BudgetLineItemsPost201Response**](RestV10BudgetLineItemsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Currency |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_budget_line_items_sync_post**
> List[RestV11BudgetLineItemsPost201Response] rest_v10_budget_line_items_sync_post(procore_company_id, body120)

Sync Budget Line Items

Create or update multiple Budget Line Items

### Example


```python
import procore_sdk
from procore_sdk.models.body120 import Body120
from procore_sdk.models.rest_v11_budget_line_items_post201_response import RestV11BudgetLineItemsPost201Response
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body120 = procore_sdk.Body120() # Body120 | 

    try:
        # Sync Budget Line Items
        api_response = api_instance.rest_v10_budget_line_items_sync_post(procore_company_id, body120)
        print("The response of ConstructionFinancialsBudgetBudgetLineItemsApi->rest_v10_budget_line_items_sync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetLineItemsApi->rest_v10_budget_line_items_sync_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body120** | [**Body120**](Body120.md)|  | 

### Return type

[**List[RestV11BudgetLineItemsPost201Response]**](RestV11BudgetLineItemsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Currency |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_budget_line_items_id_get**
> RestV11BudgetLineItemsPost201Response rest_v11_budget_line_items_id_get(procore_company_id, id, project_id)

Show Budget Line Item

Return information about a Budget Line Item.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_budget_line_items_post201_response import RestV11BudgetLineItemsPost201Response
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Budget Line Item
        api_response = api_instance.rest_v11_budget_line_items_id_get(procore_company_id, id, project_id)
        print("The response of ConstructionFinancialsBudgetBudgetLineItemsApi->rest_v11_budget_line_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetLineItemsApi->rest_v11_budget_line_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV11BudgetLineItemsPost201Response**](RestV11BudgetLineItemsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_budget_line_items_id_patch**
> RestV11BudgetLineItemsPost201Response rest_v11_budget_line_items_id_patch(procore_company_id, id, body117)

Update Budget Line Item

Update a line item of a specified budget.

### Example


```python
import procore_sdk
from procore_sdk.models.body117 import Body117
from procore_sdk.models.rest_v11_budget_line_items_post201_response import RestV11BudgetLineItemsPost201Response
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    body117 = procore_sdk.Body117() # Body117 | 

    try:
        # Update Budget Line Item
        api_response = api_instance.rest_v11_budget_line_items_id_patch(procore_company_id, id, body117)
        print("The response of ConstructionFinancialsBudgetBudgetLineItemsApi->rest_v11_budget_line_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetLineItemsApi->rest_v11_budget_line_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **body117** | [**Body117**](Body117.md)|  | 

### Return type

[**RestV11BudgetLineItemsPost201Response**](RestV11BudgetLineItemsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_budget_line_items_post**
> RestV11BudgetLineItemsPost201Response rest_v11_budget_line_items_post(procore_company_id, body116)

Create Budget Line Item

Add a new line item to a budget.

### Example


```python
import procore_sdk
from procore_sdk.models.body116 import Body116
from procore_sdk.models.rest_v11_budget_line_items_post201_response import RestV11BudgetLineItemsPost201Response
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body116 = procore_sdk.Body116() # Body116 | 

    try:
        # Create Budget Line Item
        api_response = api_instance.rest_v11_budget_line_items_post(procore_company_id, body116)
        print("The response of ConstructionFinancialsBudgetBudgetLineItemsApi->rest_v11_budget_line_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetLineItemsApi->rest_v11_budget_line_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body116** | [**Body116**](Body116.md)|  | 

### Return type

[**RestV11BudgetLineItemsPost201Response**](RestV11BudgetLineItemsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


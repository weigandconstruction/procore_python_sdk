# procore_sdk.ConstructionFinancialsBudgetBudgetViewSnapshotsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_budget_view_snapshots_get**](ConstructionFinancialsBudgetBudgetViewSnapshotsApi.md#rest_v10_budget_view_snapshots_get) | **GET** /rest/v1.0/budget_view_snapshots | List Budget View Snapshots
[**rest_v10_budget_view_snapshots_post**](ConstructionFinancialsBudgetBudgetViewSnapshotsApi.md#rest_v10_budget_view_snapshots_post) | **POST** /rest/v1.0/budget_view_snapshots | Create a Budget Snapshot.


# **rest_v10_budget_view_snapshots_get**
> List[RestV10BudgetViewSnapshotsGet200ResponseInner] rest_v10_budget_view_snapshots_get(procore_company_id, project_id, page=page, per_page=per_page)

List Budget View Snapshots

Return a list of all Budget View Snapshots for a project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_budget_view_snapshots_get200_response_inner import RestV10BudgetViewSnapshotsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetViewSnapshotsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Budget View Snapshots
        api_response = api_instance.rest_v10_budget_view_snapshots_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsBudgetBudgetViewSnapshotsApi->rest_v10_budget_view_snapshots_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetViewSnapshotsApi->rest_v10_budget_view_snapshots_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10BudgetViewSnapshotsGet200ResponseInner]**](RestV10BudgetViewSnapshotsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_budget_view_snapshots_post**
> RestV10BudgetViewSnapshotsPost201Response rest_v10_budget_view_snapshots_post(procore_company_id, rest_v10_budget_view_snapshots_post_request)

Create a Budget Snapshot.

Create a new Budget Snapshot for the Project and Budget. This is rate limited to one request per hour for each Project and Budget Template pair.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_budget_view_snapshots_post201_response import RestV10BudgetViewSnapshotsPost201Response
from procore_sdk.models.rest_v10_budget_view_snapshots_post_request import RestV10BudgetViewSnapshotsPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetViewSnapshotsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rest_v10_budget_view_snapshots_post_request = procore_sdk.RestV10BudgetViewSnapshotsPostRequest() # RestV10BudgetViewSnapshotsPostRequest | 

    try:
        # Create a Budget Snapshot.
        api_response = api_instance.rest_v10_budget_view_snapshots_post(procore_company_id, rest_v10_budget_view_snapshots_post_request)
        print("The response of ConstructionFinancialsBudgetBudgetViewSnapshotsApi->rest_v10_budget_view_snapshots_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetViewSnapshotsApi->rest_v10_budget_view_snapshots_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rest_v10_budget_view_snapshots_post_request** | [**RestV10BudgetViewSnapshotsPostRequest**](RestV10BudgetViewSnapshotsPostRequest.md)|  | 

### Return type

[**RestV10BudgetViewSnapshotsPost201Response**](RestV10BudgetViewSnapshotsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit - The total number of requests per 60-minute window <br>  * X-Rate-Limit-Remaining - The number of requests you are allowed to make in the current 60-minute window. <br>  * X-Rate-Limit-Reset - The Unix timestamp for when the next window begins. <br>  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


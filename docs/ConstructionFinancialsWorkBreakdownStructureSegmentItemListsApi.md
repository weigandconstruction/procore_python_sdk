# procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentItemListsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_lists_get**](ConstructionFinancialsWorkBreakdownStructureSegmentItemListsApi.md#rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_lists_get) | **GET** /rest/v1.0/companies/{company_id}/work_breakdown_structure/segments/{segment_id}/lists | List Company WBS Segment Item Lists


# **rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_lists_get**
> List[RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdListsGet200ResponseInner] rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_lists_get(procore_company_id, company_id, segment_id)

List Company WBS Segment Item Lists

List Segment Item Lists for a specific segment

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_lists_get200_response_inner import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdListsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentItemListsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    segment_id = 56 # int | Segment ID

    try:
        # List Company WBS Segment Item Lists
        api_response = api_instance.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_lists_get(procore_company_id, company_id, segment_id)
        print("The response of ConstructionFinancialsWorkBreakdownStructureSegmentItemListsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_lists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentItemListsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_lists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **segment_id** | **int**| Segment ID | 

### Return type

[**List[RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdListsGet200ResponseInner]**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdListsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


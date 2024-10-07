# procore_sdk.QualitySafetyInspectionsPotentialPointsOfContactApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_checklist_potential_points_of_contact_get**](QualitySafetyInspectionsPotentialPointsOfContactApi.md#rest_v10_checklist_potential_points_of_contact_get) | **GET** /rest/v1.0/checklist/potential_points_of_contact | List Potential Points of Contact


# **rest_v10_checklist_potential_points_of_contact_get**
> List[ChecklistPotentialPointOfContact] rest_v10_checklist_potential_points_of_contact_get(procore_company_id, project_id, vendor_id=vendor_id)

List Potential Points of Contact

Lists Potential Points of Contact in a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_potential_point_of_contact import ChecklistPotentialPointOfContact
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
    api_instance = procore_sdk.QualitySafetyInspectionsPotentialPointsOfContactApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    vendor_id = 56 # int | Vendor ID (optional)

    try:
        # List Potential Points of Contact
        api_response = api_instance.rest_v10_checklist_potential_points_of_contact_get(procore_company_id, project_id, vendor_id=vendor_id)
        print("The response of QualitySafetyInspectionsPotentialPointsOfContactApi->rest_v10_checklist_potential_points_of_contact_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsPotentialPointsOfContactApi->rest_v10_checklist_potential_points_of_contact_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **vendor_id** | **int**| Vendor ID | [optional] 

### Return type

[**List[ChecklistPotentialPointOfContact]**](ChecklistPotentialPointOfContact.md)

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


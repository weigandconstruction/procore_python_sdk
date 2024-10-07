# RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200Response

Bid Package Documents

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**title** | **str** | Bid package title | [optional] 
**files** | [**List[RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInner]**](RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInner.md) | List of files, attached to the bid package | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response import RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200Response from a JSON string
rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_instance = RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200Response.to_json())

# convert the object into a dict
rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_dict = rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200Response from a dict
rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_from_dict = RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200Response.from_dict(rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | Size of the file in bytes | [optional] 
**file_path** | **str** | Name of the file (as would be presented in bid package zip) | [optional] 
**s3_source** | **str** | URI, where the file is accessible at. Could have limited lifetime | [optional] 
**type** | **str** | type of the file | [optional] 
**drawing** | [**RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing**](RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_files_inner import RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInner from a JSON string
rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_files_inner_instance = RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_files_inner_dict = rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_files_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInner from a dict
rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_files_inner_from_dict = RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInner.from_dict(rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



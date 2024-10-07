# RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing

Metadata about drawing (if file is drawing)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dpi** | **float** | DPI of the drawing | [optional] 
**revision** | **str** | Revision property of the drawing | [optional] 
**drawing_set_id** | **float** | ID of the drawing set | [optional] 
**drawing_id** | **float** | ID of the drawing | [optional] 
**width** | **float** | Width of the drawing, in pixels | [optional] 
**height** | **float** | Height of the drawing, in pixels | [optional] 
**png_s3_source** | **str** | URI, where the drawing, converted to PNG, is accessible at. Could have limited lifetime | [optional] 
**thumbnail_url** | **str** | URI, where the drawing&#39;s thumbnail is accessible at. Could have limited lifetime | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_files_inner_drawing import RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing from a JSON string
rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_files_inner_drawing_instance = RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing.to_json())

# convert the object into a dict
rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_files_inner_drawing_dict = rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_files_inner_drawing_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing from a dict
rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_files_inner_drawing_from_dict = RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing.from_dict(rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_files_inner_drawing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



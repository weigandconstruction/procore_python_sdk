# RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsBidFormIdBidLevelingGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | [optional] 
**project_id** | **int** | Project ID | [optional] 
**accounting_method** | **str** |  | [optional] 
**company_name** | **str** | Company Name | [optional] 
**project_name** | **str** | Project Name | [optional] 
**base_bid_section** | [**BidFormBaseBidSection**](BidFormBaseBidSection.md) |  | [optional] 
**alternates_section** | [**BidFormBaseBidSection**](BidFormBaseBidSection.md) |  | [optional] 
**lump_sum_enabled** | **bool** | Lump Sum Enabled | [optional] 
**title** | **str** | Title | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get200_response import RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsBidFormIdBidLevelingGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsBidFormIdBidLevelingGet200Response from a JSON string
rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get200_response_instance = RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsBidFormIdBidLevelingGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsBidFormIdBidLevelingGet200Response.to_json())

# convert the object into a dict
rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get200_response_dict = rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get200_response_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsBidFormIdBidLevelingGet200Response from a dict
rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get200_response_from_dict = RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsBidFormIdBidLevelingGet200Response.from_dict(rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# BusinessNormalView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID for the business | [optional] 
**name** | **str** | Name of the Business | [optional] 
**dba** | **str** | Business Name DBA (Doing Business As) | [optional] 
**website** | **str** | Primary URL for the business website | [optional] 
**about** | **str** | About the Business text | [optional] 
**published** | **bool** | Indicates whether the Business has been publically published on PCN | [optional] 
**primary_slug** | **str** | Slug for Business | [optional] 
**logo_url** | **str** | URL link to Logo for the Business | [optional] 
**source** | [**BusinessNormalViewSource**](BusinessNormalViewSource.md) |  | [optional] 
**addresses** | [**List[BusinessNormalViewAddressesInner]**](BusinessNormalViewAddressesInner.md) | Addresses for the Business. These are also reflected in Offices for the Company. | [optional] 
**provided_services** | [**List[BusinessNormalViewProvidedServicesInner]**](BusinessNormalViewProvidedServicesInner.md) | Services the Business Provides | [optional] 
**construction_sectors** | **List[str]** | Construction Sectors this Business works in | [optional] 
**business_types** | **List[str]** | Business Types this Business falls under | [optional] 
**project_types** | **List[str]** | Project Types this Business falls under | [optional] 
**classifications** | [**List[BusinessNormalViewClassificationsInner]**](BusinessNormalViewClassificationsInner.md) | Classifications this Business falls under | [optional] 
**coverage_areas** | [**List[BusinessNormalViewCoverageAreasInner]**](BusinessNormalViewCoverageAreasInner.md) | Business area coverage | [optional] 
**claimed** | **bool** | Indicates whether the Business has been claimed by a user | [optional] 
**tags** | [**BusinessNormalViewTags**](BusinessNormalViewTags.md) |  | [optional] 
**start_of_operations** | **date** | Date when the business started operations | [optional] 

## Example

```python
from procore_sdk.models.business_normal_view import BusinessNormalView

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessNormalView from a JSON string
business_normal_view_instance = BusinessNormalView.from_json(json)
# print the JSON string representation of the object
print(BusinessNormalView.to_json())

# convert the object into a dict
business_normal_view_dict = business_normal_view_instance.to_dict()
# create an instance of BusinessNormalView from a dict
business_normal_view_from_dict = BusinessNormalView.from_dict(business_normal_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



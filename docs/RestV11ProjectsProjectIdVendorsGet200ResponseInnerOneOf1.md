# RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address | [optional] 
**business_id** | **str** | Business id | [optional] 
**business_phone** | **str** | Business phone | [optional] 
**business_register** | [**NormalViewBusinessRegister**](NormalViewBusinessRegister.md) |  | [optional] 
**city** | **str** | City | [optional] 
**country_code** | **str** | Country code (ISO-3166 Alpha-2 format) | [optional] 
**email_address** | **str** | Email address | [optional] 
**fax_number** | **str** | Fax number | [optional] 
**is_active** | **bool** | Active status | [optional] 
**logo** | **str** | Logo url | [optional] 
**state_code** | **str** | State code (ISO-3166 Alpha-2 format) | [optional] 
**trade_name** | **str** | Vendor&#39;s Trade Name, also known as Doing Business As (DBA). | [optional] 
**zip** | **str** | Zip code | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_vendors_get200_response_inner_one_of1 import RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf1 from a JSON string
rest_v11_projects_project_id_vendors_get200_response_inner_one_of1_instance = RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf1.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf1.to_json())

# convert the object into a dict
rest_v11_projects_project_id_vendors_get200_response_inner_one_of1_dict = rest_v11_projects_project_id_vendors_get200_response_inner_one_of1_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf1 from a dict
rest_v11_projects_project_id_vendors_get200_response_inner_one_of1_from_dict = RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf1.from_dict(rest_v11_projects_project_id_vendors_get200_response_inner_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ProjectVendor1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbreviated_name** | **str** | Abbreviated name | [optional] 
**address** | **str** | Address | [optional] 
**authorized_bidder** | **bool** | Authorized bidder status | [optional] 
**business_phone** | **str** | Business phone | [optional] 
**city** | **str** | City | [optional] 
**country_code** | **str** | Country code (ISO-3166 Alpha-2 format) | [optional] 
**email_address** | **str** | Email address | [optional] 
**fax_number** | **str** | Fax number | [optional] 
**is_active** | **bool** | Active status | [optional] 
**labor_union** | **str** | Labor union | [optional] 
**license_number** | **str** | License number | [optional] 
**mobile_phone** | **str** | Mobile phone | [optional] 
**name** | **str** | Name | [optional] 
**non_union_prevailing_wage** | **bool** | Non union prevailing wage status | [optional] 
**notes** | **str** | Notes (notes/keywords/tags) | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**origin_data** | **str** | Origin Data | [optional] 
**origin_code** | **str** | Origin Code | [optional] 
**parent_id** | **int** | Parent Vendor ID. Cannot be the same as ID. Only two levels of hierarchy are supported (parent/child). | [optional] 
**prequalified** | **bool** | Prequalified status | [optional] [default to False]
**primary_contact_id** | **int** | Primary Contact ID | [optional] 
**state_code** | **str** | State code (ISO-3166 Alpha-2 format) | [optional] 
**trade_name** | **str** | Vendor&#39;s Trade Name, also known as Doing Business As (DBA). | [optional] 
**union_member** | **bool** | Union member status | [optional] 
**website** | **str** | Website url | [optional] 
**zip** | **str** | Zip code | [optional] 
**bidding** | [**ProjectVendor1Bidding**](ProjectVendor1Bidding.md) |  | [optional] 

## Example

```python
from procore_sdk.models.project_vendor1 import ProjectVendor1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectVendor1 from a JSON string
project_vendor1_instance = ProjectVendor1.from_json(json)
# print the JSON string representation of the object
print(ProjectVendor1.to_json())

# convert the object into a dict
project_vendor1_dict = project_vendor1_instance.to_dict()
# create an instance of ProjectVendor1 from a dict
project_vendor1_from_dict = ProjectVendor1.from_dict(project_vendor1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



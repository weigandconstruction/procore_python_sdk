# ProjectVendor1Bidding

Bidding statuses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affirmative_action** | **bool** |  | [optional] [default to False]
**small_business** | **bool** |  | [optional] [default to False]
**african_american_business** | **bool** |  | [optional] [default to False]
**hispanic_business** | **bool** |  | [optional] [default to False]
**womens_business** | **bool** |  | [optional] [default to False]
**historically_underutilized_business** | **bool** |  | [optional] [default to False]
**sdvo_business** | **bool** |  | [optional] [default to False]
**certified_business_enterprise** | **bool** |  | [optional] [default to False]
**asian_american_business** | **bool** |  | [optional] [default to False]
**native_american_business** | **bool** |  | [optional] [default to False]
**disadvantaged_business** | **bool** |  | [optional] [default to False]
**minority_business_enterprise** | **bool** |  | [optional] [default to False]
**eight_a_business** | **bool** |  | [optional] [default to False]

## Example

```python
from procore_sdk.models.project_vendor1_bidding import ProjectVendor1Bidding

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectVendor1Bidding from a JSON string
project_vendor1_bidding_instance = ProjectVendor1Bidding.from_json(json)
# print the JSON string representation of the object
print(ProjectVendor1Bidding.to_json())

# convert the object into a dict
project_vendor1_bidding_dict = project_vendor1_bidding_instance.to_dict()
# create an instance of ProjectVendor1Bidding from a dict
project_vendor1_bidding_from_dict = ProjectVendor1Bidding.from_dict(project_vendor1_bidding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



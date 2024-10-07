# OfficeLogo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Use :name, :filename to be deprecated | [optional] 
**url** | **str** |  | [optional] 
**filename** | **str** | :filename to be deprecated, use :name | [optional] 

## Example

```python
from procore_sdk.models.office_logo import OfficeLogo

# TODO update the JSON string below
json = "{}"
# create an instance of OfficeLogo from a JSON string
office_logo_instance = OfficeLogo.from_json(json)
# print the JSON string representation of the object
print(OfficeLogo.to_json())

# convert the object into a dict
office_logo_dict = office_logo_instance.to_dict()
# create an instance of OfficeLogo from a dict
office_logo_from_dict = OfficeLogo.from_dict(office_logo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



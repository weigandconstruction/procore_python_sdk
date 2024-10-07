# Office

Office

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Office id | [optional] 
**name** | **str** | Office name | [optional] 
**address** | **str** | Office address | [optional] 
**city** | **str** | Office city | [optional] 
**state_code** | **str** | Office state code (ISO-3166 Alpha-2 format) | [optional] 
**country_code** | **str** | Office country code (ISO-3166 Alpha-2 format) | [optional] 
**zip** | **str** | Office zip | [optional] 
**phone** | **str** | Office phone | [optional] 
**fax** | **str** | Office fax | [optional] 
**division** | **str** | Office division | [optional] 
**logo** | [**OfficeLogo**](OfficeLogo.md) |  | [optional] 

## Example

```python
from procore_sdk.models.office import Office

# TODO update the JSON string below
json = "{}"
# create an instance of Office from a JSON string
office_instance = Office.from_json(json)
# print the JSON string representation of the object
print(Office.to_json())

# convert the object into a dict
office_dict = office_instance.to_dict()
# create an instance of Office from a dict
office_from_dict = Office.from_dict(office_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Office2

Office object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Office | 
**address** | **str** | The Address of the Office | [optional] 
**city** | **str** | The City of the Office | [optional] 
**state_code** | **str** | The State Code of the Office (ISO-3166 Alpha-2 format) | [optional] 
**country_code** | **str** | The Country Code of the Office (ISO-3166 Alpha-2 format) | [optional] 
**zip** | **str** | The Zip of the Office | [optional] 
**phone** | **str** | The Phone of the Office | [optional] 
**fax** | **str** | The Fax of the Office | [optional] 
**division** | **str** | The Division of the Office | [optional] 
**logo** | **bytearray** | A photo file of the Office Logo. To upload an office logo you must upload whole payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;office[logo]&#x60; as file. | [optional] 

## Example

```python
from procore_sdk.models.office2 import Office2

# TODO update the JSON string below
json = "{}"
# create an instance of Office2 from a JSON string
office2_instance = Office2.from_json(json)
# print the JSON string representation of the object
print(Office2.to_json())

# convert the object into a dict
office2_dict = office2_instance.to_dict()
# create an instance of Office2 from a dict
office2_from_dict = Office2.from_dict(office2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



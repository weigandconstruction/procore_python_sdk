# InspectionItemSignatureCapturedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the user. | [optional] 
**login** | **str** | The email address of the user that is used to log in. | [optional] 
**name** | **str** | The name of the user. | [optional] 
**company_name** | **str** | User&#39;s Company Name | [optional] 

## Example

```python
from procore_sdk.models.inspection_item_signature_captured_by import InspectionItemSignatureCapturedBy

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionItemSignatureCapturedBy from a JSON string
inspection_item_signature_captured_by_instance = InspectionItemSignatureCapturedBy.from_json(json)
# print the JSON string representation of the object
print(InspectionItemSignatureCapturedBy.to_json())

# convert the object into a dict
inspection_item_signature_captured_by_dict = inspection_item_signature_captured_by_instance.to_dict()
# create an instance of InspectionItemSignatureCapturedBy from a dict
inspection_item_signature_captured_by_from_dict = InspectionItemSignatureCapturedBy.from_dict(inspection_item_signature_captured_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



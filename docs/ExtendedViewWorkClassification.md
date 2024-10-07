# ExtendedViewWorkClassification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | The name of the classification | [optional] 

## Example

```python
from procore_sdk.models.extended_view_work_classification import ExtendedViewWorkClassification

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedViewWorkClassification from a JSON string
extended_view_work_classification_instance = ExtendedViewWorkClassification.from_json(json)
# print the JSON string representation of the object
print(ExtendedViewWorkClassification.to_json())

# convert the object into a dict
extended_view_work_classification_dict = extended_view_work_classification_instance.to_dict()
# create an instance of ExtendedViewWorkClassification from a dict
extended_view_work_classification_from_dict = ExtendedViewWorkClassification.from_dict(extended_view_work_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



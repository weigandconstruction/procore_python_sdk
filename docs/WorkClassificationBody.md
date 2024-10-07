# WorkClassificationBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_classification** | [**WorkClassification**](WorkClassification.md) |  | 

## Example

```python
from procore_sdk.models.work_classification_body import WorkClassificationBody

# TODO update the JSON string below
json = "{}"
# create an instance of WorkClassificationBody from a JSON string
work_classification_body_instance = WorkClassificationBody.from_json(json)
# print the JSON string representation of the object
print(WorkClassificationBody.to_json())

# convert the object into a dict
work_classification_body_dict = work_classification_body_instance.to_dict()
# create an instance of WorkClassificationBody from a dict
work_classification_body_from_dict = WorkClassificationBody.from_dict(work_classification_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



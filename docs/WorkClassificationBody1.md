# WorkClassificationBody1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_classification** | [**WorkClassification2**](WorkClassification2.md) |  | 

## Example

```python
from procore_sdk.models.work_classification_body1 import WorkClassificationBody1

# TODO update the JSON string below
json = "{}"
# create an instance of WorkClassificationBody1 from a JSON string
work_classification_body1_instance = WorkClassificationBody1.from_json(json)
# print the JSON string representation of the object
print(WorkClassificationBody1.to_json())

# convert the object into a dict
work_classification_body1_dict = work_classification_body1_instance.to_dict()
# create an instance of WorkClassificationBody1 from a dict
work_classification_body1_from_dict = WorkClassificationBody1.from_dict(work_classification_body1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



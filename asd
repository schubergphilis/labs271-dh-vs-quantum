{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "VisualEditor0",
			"Effect": "Allow",
			"Action": "braket:GetDevice",
			"Resource": "*"
		},
		{
			"Sid": "VisualEditor1",
			"Effect": "Allow",
			"Action": "sagemaker:ListNotebookInstances",
			"Resource": "*"
		},
		{
			"Sid": "VisualEditor2",
			"Effect": "Allow",
			"Action": [
				"sagemaker:StopNotebookInstance",
				"sagemaker:CreatePresignedNotebookInstanceUrl",
				"sagemaker:DescribeNotebookInstance",
				"sagemaker:StartNotebookInstance"
			],
			"Resource": "arn:aws:sagemaker:*:758793629524:notebook-instance/amazon-braket-${aws:username}"
		}
	]
}